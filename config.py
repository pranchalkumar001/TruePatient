import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')
    DATABASE_URI = os.environ.get('DATABASE_URI')
    # Add other model settings as needed
