from flask import render_template, Blueprint, jsonify
from app.services.UserService import UserService

api_bp = Blueprint('api', __name__)

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
