import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.environ.get('FLASK_ENV', 'development')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')