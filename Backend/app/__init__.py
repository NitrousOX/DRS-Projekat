from flask import Flask
from flask_socketio import SocketIO
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from .api.routes import init_routes, api_bp
from .api.sockets import init_sockets

# Load environment variables from .env file
load_dotenv()

# Initialize app and socketio
socketio = SocketIO()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py or .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    # MongoDB connection setup
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    app.config['MONGO_URI'] = mongo_uri

    # Initialize MongoDB client
    mongo_client = MongoClient(mongo_uri)
    app.db = mongo_client['DRS']

    # Initialize SocketIO with app
    socketio.init_app(app)

    # Register routes and sockets
    app.register_blueprint(api_bp, url_prefix='/api')
    init_routes(app)
    init_sockets(socketio)

    return app