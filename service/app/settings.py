import os

FLASK_APP = 'postgres'
FLASK_ENV = 'development'

DEBUG = False
SECRET_KEY = os.environ.get('POSTGRES_PASSWORD')

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:testpassword@postgres:5432/postgres" #os.environ.get('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False
