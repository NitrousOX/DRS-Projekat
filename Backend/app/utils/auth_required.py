from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt

def jwt_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get('isAdmin') is not True:
            return jsonify({"msg": "Access forbidden. Admins only."}), 403
        return fn(*args, **kwargs)
    return wrapper
