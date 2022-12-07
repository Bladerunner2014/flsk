from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from log.models import User
from flask_login import current_user


class SignUpForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),
        Length(min=4, max=25, message='username must be between 4 and 25 characters')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password', validators=[DataRequired(),
        EqualTo('password', message='passwords must match')])


class LoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
