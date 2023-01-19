from datetime import datetime

from ..common.jsonserializer import JsonSerializer
from ..common.db import db


class UserJsonSerializer(JsonSerializer):

    __json_public__ = ['id', 'firstname', 'lastname', 'job_title', 'email', 'description']


class UserModel(UserJsonSerializer, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
