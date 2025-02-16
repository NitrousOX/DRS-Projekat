from flask import Blueprint, request, jsonify
from app.services.UserService import UserService

user_bp = Blueprint('user', __name__, url_prefix='/users')

#TODO: Fix error handling like  in the delete

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify(users)


@user_bp.route('/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/email/<email>', methods=['GET'])
def get_user_by_email(email):
    user = UserService.get_user_by_email(email)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user_id = UserService.create_user(data)
    return jsonify({'user_id': user_id}), 201


@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    success = UserService.update_user(user_id, data)
    if success:
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = UserService.delete_user(user_id)
    return jsonify(response)
