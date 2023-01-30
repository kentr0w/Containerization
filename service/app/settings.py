import os

FLASK_APP = 'postgres'
FLASK_ENV = 'development'

DEBUG = False
SECRET_KEY = "superkey"

PASSWORD = os.environ.get('POSTGRES_PASSWORD')
print(os.environ.get('POSTGRES_PASSWORD'))
USER = os.environ.get('POSTGRES_USER')
HOSTNAME = os.environ.get('POSTGRES_HOSTNAME')
PORT = os.environ.get('POSTGRES_PORT')
DB = os.environ.get('POSTGRES_DB')

SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False
