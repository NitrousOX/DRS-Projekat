from functools import wraps
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.UserService import UserService
from app.utils.auth_required import jwt_admin
user_bp = Blueprint('user', __name__, url_prefix='/users')


#GET ALL
@user_bp.route('/', methods=['GET'])
@jwt_required()
@jwt_admin
def get_all_users():
    response = UserService.get_all_users()
    return jsonify(response.value), response.status_code

#GET BY ID
@user_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    response = UserService.get_user_by_id(user_id)
    return jsonify(response.value), response.status_code

#GET BY EMAIL
@user_bp.route('/email/<email>', methods=['GET'])
@jwt_required()
def get_user_by_email(email):
    response = UserService.get_user_by_email(email)
    return jsonify(response.value), response.status_code

#CREATE
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    response = UserService.create_user(data)
    return jsonify(response.value), response.status_code

#UPDATE
@user_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.json
    response = UserService.update_user(user_id, data)
    return jsonify(response.value), response.status_code

#DELETE
@user_bp.route('/<user_id>', methods=['DELETE'])
@jwt_required()
@jwt_admin
def delete_user(user_id):
    response = UserService.delete_user(user_id)
    return jsonify(response.value), response.status_code

#APPROVE REGISTRAION
@user_bp.route('/approve/<user_id>', methods=['PUT'])
@jwt_required()
@jwt_admin
def approve_user(user_id):
    response = UserService.approve_registration(user_id=user_id)
    return jsonify(response.value), response.status_code

#REJECT REGISTRAION
@user_bp.route('/reject/<user_id>', methods=['PUT'])
@jwt_required()
@jwt_admin
def reject_user(user_id):
    response = UserService.reject_registration(user_id=user_id)
    return jsonify(response.value), response.status_code