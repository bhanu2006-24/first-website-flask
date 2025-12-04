import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret'
    DEBUG = os.environ.get('DEBUG') == 'True'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
