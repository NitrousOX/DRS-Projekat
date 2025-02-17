from app.repo.UserRepo import UserRepository
from app.models.User import User
from pymongo.errors import PyMongoError
from app.models.ApiResponse import ApiResponse, STATUS_CODES

class UserService:
    @staticmethod
    def get_all_users():
        try:
            users = UserRepository.get_all_data()
            if users:
                return ApiResponse(users, STATUS_CODES["SUCCESS"])
            else:
                return ApiResponse("No users found.", STATUS_CODES["NOT_FOUND"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserRepository.get_user_by_id(user_id)
            if user:
                return ApiResponse(user, STATUS_CODES["SUCCESS"])
            else:
                return ApiResponse(f"User with ID {user_id} not found.", STATUS_CODES["NOT_FOUND"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])

    @staticmethod
    def get_user_by_email(email):
        try:
            user = UserRepository.get_user_by_email(email)
            if user:
                return ApiResponse(user, STATUS_CODES["SUCCESS"])
            else:
                return ApiResponse(f"User with email {email} not found.", STATUS_CODES["NOT_FOUND"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])

    @staticmethod
    def create_user(user_data):
        try:
            user = User(**user_data)
            existing_user = UserRepository.get_user_by_email(user.email)
            if existing_user:
                return ApiResponse("A user with this email already exists.", STATUS_CODES["CONFLICT"])
            user_id = UserRepository.create_user(user)
            return ApiResponse({"message": "User created successfully", "user_id": str(user_id)}, STATUS_CODES["SUCCESS"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])
        except TypeError as e:
            return ApiResponse(f"Missing values: {str(e)}", STATUS_CODES["BAD_REQUEST"])
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])

    @staticmethod
    def update_user(user_id, updated_data):
        try:
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return ApiResponse(f"User with ID {user_id} not found.", STATUS_CODES["NOT_FOUND"])
            updated_user = User(**updated_data)
            success = UserRepository.update_user(user_id, updated_user.to_dict())
            if success:
                return ApiResponse("User updated successfully", STATUS_CODES["SUCCESS"])
            else:
                return ApiResponse("Failed to update user.", STATUS_CODES["INTERNAL_SERVER_ERROR"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])
        except TypeError as e:
            return ApiResponse(f"Missing values: {str(e)}", STATUS_CODES["BAD_REQUEST"])
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])

    @staticmethod
    def delete_user(user_id):
        try:
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return ApiResponse(f"User with ID {user_id} not found.", STATUS_CODES["NOT_FOUND"])
            success = UserRepository.delete_user(user_id)
            if success:
                return ApiResponse("User deleted successfully", STATUS_CODES["SUCCESS"])
            else:
                return ApiResponse("Failed to delete user.", STATUS_CODES["INTERNAL_SERVER_ERROR"])
        except PyMongoError as e:
            return ApiResponse(f"Database error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])
        except Exception as e:
            return ApiResponse(f"Unexpected error: {str(e)}", STATUS_CODES["INTERNAL_SERVER_ERROR"])