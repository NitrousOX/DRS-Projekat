from flask import jsonify
from app.repo.UserRepo import UserRepository
from app.models.ApiResponse import ApiResponse, StatusCodes
from app.services.JwtService import create_tokens

class LoginService:
    @staticmethod
    def login(email: str, password: str):
        if not email or not password:
            return ApiResponse({"msg": "Email or password was empty!"}, StatusCodes.BAD_REQUEST)
        found_user = UserRepository.get_user_by_email(email=email)
        if not found_user:
            return ApiResponse({"msg": "Wrong password or email"}, StatusCodes.NOT_FOUND)
        
        # Assuming found_user is a dictionary with 'password', 'id', 'email', and 'role'
        if found_user['password'] != password:
            return ApiResponse({"msg": "Wrong password or email"}, StatusCodes.NOT_FOUND)

        user_info = {
            'id': str(found_user['_id']),
            'email': found_user['email'],
            'isAdmin': found_user['isAdmin']
        }
        tokens = create_tokens(user_info)
        if not tokens:
            return ApiResponse({"msg": "Failed to create tokens"}, StatusCodes.INTERNAL_SERVER_ERROR)

        return ApiResponse(tokens, StatusCodes.SUCCESS)