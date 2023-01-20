from flask import Blueprint, jsonify
from http import HTTPStatus

from ..common.error_http import error_http
from ..services_list import UsersServiceInstance
from ..users.users_forms import AddUserForm

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def list_all():
    result_query = UsersServiceInstance.get_all()
    return jsonify({'keys': [url.to_json() for url in result_query]}), 200

@bp.route('/', methods=['POST'])
def add():
    form = AddUserForm()

from flask import Blueprint, jsonify
from http import HTTPStatus

from ..common.error_http import error_http
from ..services_list import UsersServiceInstance
from ..users.users_forms import AddUserForm

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def list_all():
    result_query = UsersServiceInstance.get_all()
    return jsonify({'keys': [url.to_json() for url in result_query]}), 200

@bp.route('/', methods=['POST'])
def add():
    form = AddUserForm()

    if form.validate_on_submit():

        firstname = form.firstname.data
        lastname = form.lastname.data
        job_title = form.job_title.data
        email = form.email.data
        description = form.description.data

        result_query = UsersServiceInstance.create(**{
            'firstname': firstname,
            'lastname': lastname,
            'job_title': job_title,
            'email': email,
            'description':description
        })
        return {'key': result_query.to_json()}, 201

    return error_http(HTTPStatus.BAD_REQUEST)
    
    
    
    
    
    
    
