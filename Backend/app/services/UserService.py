from app.repo.UserRepo import UserRepository
from app.models.User import User
from pymongo.errors import PyMongoError

#TODO: Finish checks and edge cases

class UserService:
    @staticmethod
    def get_all_users():
        try:
            users = UserRepository.get_all_data()
            return users if users else {"error": "No users found."}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = UserRepository.get_user_by_id(user_id)
            if user:
                return user
            else:
                return {"error": f"User with ID {user_id} not found."}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}

    @staticmethod
    def get_user_by_email(email):
        try:
            user = UserRepository.get_user_by_email(email)
            if user:
                return user
            else:
                return {"error": f"User with email {email} not found."}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}

    @staticmethod
    def create_user(user_data):
        try:
            # Assuming user_data is a dictionary or an object that can be converted to a User instance
            user = User(**user_data)
            
            # Check if a user with the same email already exists
            existing_user = UserRepository.get_user_by_email(user.email)
            if existing_user:
                return {"error": "A user with this email already exists."}

            user_id = UserRepository.create_user(user)
            return {"message": "User created successfully", "user_id": str(user_id)}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    @staticmethod
    def update_user(user_id, updated_data):
        try:
            # Check if the user exists first
            existing_user = UserRepository.get_user_by_id(user_id)
            if not existing_user:
                return {"error": f"User with ID {user_id} not found."}

            # Update user details
            success = UserRepository.update_user(user_id, updated_data)
            if success:
                return {"message": "User updated successfully"}
            else:
                return {"error": "Failed to update user."}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}

    @staticmethod
    def delete_user(user_id):
        try:
            # Check if the user exists first
            existing_user = UserRepository.get_user_by_id(user_id)
            
            if not existing_user:
                return {"error": f"User with ID {user_id} not found."}

            # Delete the user
            success = UserRepository.delete_user(user_id)
            if success:
                return {"message": "User deleted successfully"}
            else:
                return {"error": "Failed to delete user."}
        except PyMongoError as e:
            return {"error": f"Database error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
