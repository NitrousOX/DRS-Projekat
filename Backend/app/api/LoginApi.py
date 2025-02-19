from flask import Blueprint, request, jsonify
from app.services.LoginService import LoginService
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, jwt_required, get_jwt_identity, create_access_token

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    api_response = LoginService.login(email, password)

    if api_response.status_code == 200:
        tokens = api_response.value
        response = jsonify({"msg":"Login successful"})
        set_access_cookies(response, tokens['access_token'])
        set_refresh_cookies(response, tokens['refresh_token'])
        return response, api_response.status_code
    else:
        return jsonify(api_response.value), api_response.status_code

@login_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200