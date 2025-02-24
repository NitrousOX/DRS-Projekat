from flask import Flask
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from pymongo import MongoClient
from dotenv import load_dotenv
from .api.UserApi import user_bp
from .api.LoginApi import login_bp
from .api.sockets import init_sockets
from app.config import Config
# Load environment variables from .env file
load_dotenv()

# Initialize app and socketio
socketio = SocketIO(cors_allowed_origins="*")
mail = Mail()

def create_app():
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    CORS(app)

    # Initialize MongoDB client
    mongo_client = MongoClient(app.config['MONGO_URI'])
    app.db = mongo_client['DRS']

    # Initialize JWT
    JWTManager(app)

    # Initialize SocketIO with app
    socketio.init_app(app)
    # Initialize Mail sending
    mail.init_app(app)

    # Register routes and sockets
    app.register_blueprint(user_bp)
    app.register_blueprint(login_bp)
    init_sockets(socketio)

    return app