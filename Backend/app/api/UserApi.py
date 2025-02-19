from functools import wraps
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.UserService import UserService
from app.utils.auth_required import jwt_admin
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    response = UserService.get_all_users()
    return jsonify(response.value), response.status_code

@user_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    response = UserService.get_user_by_id(user_id)
    return jsonify(response.value), response.status_code

@user_bp.route('/email/<email>', methods=['GET'])
@jwt_required()
def get_user_by_email(email):
    response = UserService.get_user_by_email(email)
    return jsonify(response.value), response.status_code

@user_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    data = request.json
    response = UserService.create_user(data)
    return jsonify(response.value), response.status_code

@user_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.json
    response = UserService.update_user(user_id, data)
    return jsonify(response.value), response.status_code

@user_bp.route('/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    response = UserService.delete_user(user_id)
    return jsonify(response.value), response.status_code
