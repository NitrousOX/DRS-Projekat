import os
from flask import Flask
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from .api.UserApi import user_bp
from .api.LoginApi import login_bp
from .api.sockets import init_sockets

# Load environment variables from .env file
load_dotenv()

# Initialize app and socketio
socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    CORS(app)

    # Load configuration from config.py or .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

    # Secure cookie settings for JWT
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SECURE'] = True  # Only send cookies over HTTPS
    app.config['JWT_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to cookies
    app.config['JWT_COOKIE_SAMESITE'] = 'Strict'  # CSRF protection

    # MongoDB connection setup
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    app.config['MONGO_URI'] = mongo_uri

    # Initialize MongoDB client
    mongo_client = MongoClient(mongo_uri)
    app.db = mongo_client['DRS']

    # Initialize JWT
    jwt = JWTManager(app)

    # Initialize SocketIO with app
    socketio.init_app(app)

    # Register routes and sockets
    app.register_blueprint(user_bp)
    app.register_blueprint(login_bp)
    init_sockets(socketio)

    return app