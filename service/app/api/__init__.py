from flask import Flask

from ..common.db import db
from ..middleware import HTTPMethodOverrideMiddleware
from . import users_api


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('app.settings')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(users_api.bp)

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app
