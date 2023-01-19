import os

FLASK_APP = 'app'
FLASK_ENV = 'development'

DEBUG = False
SECRET_KEY = 'super-secret-key'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False
