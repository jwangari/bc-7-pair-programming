from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LogInForm(Form):
	email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
	keep_on = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class SignUpForm(Form):
    email = StringField('Email', validators=[Required(), Email(), 
											 Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters,'
                                                                                     'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
    	Required(), EqualTo('password2', message="Your passwords do no match. Please re-enter")])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
    	if User.query.filter_by(email=field.data).first():
    		raise ValidationError('Email already registered')

    def validate_username(self, field):
    	if User.query.filter_by(username=field.data).first():
    		raise ValidationError('Username already in use')
