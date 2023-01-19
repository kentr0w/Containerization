from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddUserForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    job_title = StringField('job_title', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    description = StringField('description')
    submit = SubmitField('submit')