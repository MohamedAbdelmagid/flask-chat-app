from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


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