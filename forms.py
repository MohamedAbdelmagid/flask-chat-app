from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256

from models import User

def invalid_credentials(form, field):
	""" Check username & password in database """

	username = form.username.data
	password = field.data

	# Check validation of creds
	user = User.query.filter_by(username=username).first()
	if user is None or not pbkdf2_sha256.verify(password, user.password):
		raise ValidationError("Username or password is incorrect !!")

class RegistartionForm(FlaskForm):
	""" Registration Form """

	username = StringField('username',
		validators=[
			InputRequired(message='This field is required'),
			Length(min=4, max=25, message='Name must consist of more than 4 charactors and less than 25')
		])
	password = PasswordField('password',
		validators=[
			InputRequired(message='This field is required'),
			Length(min=4, max=25, message='Password should be more than 4 and less than 25')
		])
	confirm_password = PasswordField('confirm_password',
		validators=[
			InputRequired(message='This field is required'),
			EqualTo('password', message='Password should match')
		])
	submit_button = SubmitField('Create')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("This name is already used by someone else !!")

class LoginForm(FlaskForm):
	""" Login Form """

	username = StringField('username',
		validators=[
			InputRequired(message='This field is required'),
		])
	password = PasswordField('password',
		validators=[
			InputRequired(message='This field is required'),
			invalid_credentials
		])
	submit_button = SubmitField('Login')