# config.py
from datetime import timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', '02984y9fh923hf032h')
    
    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '1309h03hfd013whfd0wqh0i3po')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True  # Only send cookies over HTTPS
    JWT_COOKIE_HTTPONLY = True  # Prevent JavaScript access to cookies
    JWT_COOKIE_SAMESITE = 'Strict'  # CSRF protection
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    
    # MongoDB configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')