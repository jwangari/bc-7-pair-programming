from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, HiddenField
from wtforms.validators import Required

class LogInForm(Form):
	email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
	password = HiddenField('Password', validators=[Required()])
	keep_on = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class SignUpForm(Form):
	email = StringField('Email', validators=[Required(), Email(), Length(1, 64),])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = HiddenField('Password', validators=[Required(), EqualTo('password2', message="Your passwords do no match. Please re-enter")])
    password2 = HiddenField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign Up')
