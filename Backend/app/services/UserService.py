from app.repo.UserRepo import UserRepository
from app.models.User import User
from pymongo.errors import PyMongoError
from app.models.ApiResponse import ApiResponse, StatusCodes
from app.utils.EmailService import send_email
class UserService:
    @staticmethod
    def get_all_users():
        try:
            users = UserRepository.get_all_data()
            if users:
                return ApiResponse(users, StatusCodes.SUCCESS)
            else:
                return ApiResponse("No users found.", StatusCodes.NOT_FOUND)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserRepository.get_user_by_id(user_id)
            if user:
                return ApiResponse(user, StatusCodes.SUCCESS)
            else:
                return ApiResponse(f"User with ID {user_id} not found.", StatusCodes.NOT_FOUND)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_user_by_email(email):
        try:
            user = UserRepository.get_user_by_email(email)
            if user:
                return ApiResponse(user, StatusCodes.SUCCESS)
            else:
                return ApiResponse(f"User with email {email} not found.", StatusCodes.NOT_FOUND)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)

    @staticmethod
    def create_user(user_data):
        try:
            user = User(**user_data)
            existing_user = UserRepository.get_user_by_email(user.email)
            if existing_user:
                return ApiResponse("A user with this email already exists.", StatusCodes.CONFLICT)
            user_id = UserRepository.create_user(user)
            return ApiResponse({"message": "User created successfully", "user_id": str(user_id)}, StatusCodes.SUCCESS)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)
        except TypeError as e:
            return ApiResponse(f"Missing values: {str(e)}", StatusCodes.BAD_REQUEST)
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)

    @staticmethod
    def update_user(user_id, updated_data):
        try:
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return ApiResponse(f"User with ID {user_id} not found.", StatusCodes.NOT_FOUND)
            updated_user = User(**updated_data)
            success = UserRepository.update_user(user_id, updated_user.to_dict())
            if success:
                return ApiResponse("User updated successfully", StatusCodes.SUCCESS)
            else:
                return ApiResponse("Failed to update user.", StatusCodes.INTERNAL_SERVER_ERROR)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)
        except TypeError as e:
            return ApiResponse(f"Missing values: {str(e)}", StatusCodes.BAD_REQUEST)
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)

    @staticmethod
    def delete_user(user_id):
        try:
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return ApiResponse(f"User with ID {user_id} not found.", StatusCodes.NOT_FOUND)
            success = UserRepository.delete_user(user_id)
            if success:
                return ApiResponse("User deleted successfully", StatusCodes.SUCCESS)
            else:
                return ApiResponse("Failed to delete user.", StatusCodes.INTERNAL_SERVER_ERROR)
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)
        
    @staticmethod
    def update_registration_status(user_id, is_registered):
        try:
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return ApiResponse(f"User with ID {user_id} not found.", StatusCodes.NOT_FOUND)

            # Handle user registration status
            if is_registered:
                #API response
                message = "User registration approved successfully."
                status = StatusCodes.SUCCESS
                #EMAIL
                template = "account_approved_email.html"
                subject = "Account approved"
            else:
                # Delete user if not registered
                if UserRepository.delete_user(user_id):
                    message = "User registration declined and user deleted successfully."
                    status = StatusCodes.SUCCESS
                    
                    template = "account_denied_email.html"
                    subject = "Account rejected"
                else:
                    message = "User registration declined, but failed to delete the user."
                    status = StatusCodes.INTERNAL_SERVER_ERROR
                    template = None  # No email to send if deletion fails

            # Send email if the deletion was successful or if the account was approved
            if template:
                send_email(
                    subject=subject,
                    recipients=[existing_user["email"]],
                    template_name=template,
                    name=existing_user["name"],
                    url="#" if not is_registered else "#"
                )

            return ApiResponse(message, status)

        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", StatusCodes.INTERNAL_SERVER_ERROR)



    @staticmethod
    def approve_registration(user_id):
        return UserService.update_registration_status(user_id, True)
    
    
    @staticmethod
    def reject_registration(user_id):
        return UserService.update_registration_status(user_id, False)
    
    @staticmethod
    def first_login(user):
        UserRepository.update_user(user['_id'], {'firstLogin': False})
        all_admins = UserRepository.get_all_admins()
        print(all_admins)
        admin_emails = [admin['email'] for admin in all_admins]
        send_email(
            subject="User First Login",
            recipients=admin_emails,
            template_name="first_login_email.html",
            user_name=user["username"],
            user_email=user["email"]
        )
        