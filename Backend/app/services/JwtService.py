from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

def create_tokens(user_info):
    user_id = str(user_info['id'])
    access_token = create_access_token(
        identity=user_id,
        additional_claims={
            'email': user_info['email'],
            'isAdmin': user_info['isAdmin']
        }
    )
    refresh_token = create_refresh_token(identity=user_id)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }

def refresh_access_token():
    current_user = get_jwt_identity()
    return create_access_token(identity=current_user)