from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from . forms import LogInForm, SignUpForm
from ..models import User
from app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
	'''
		This view function creates a LoginForm object and uses it like a simple form.
			-When request is of type GET, the view function renders template which
				displays the form
			-When request is of type POST, the Flask WTF's validate_on_submit()
				validates the form variables and then attempts to log the user in
	'''
	form = LogInForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.keep_on.data)
			return redirect(url_for('main.new_session'))
		flash('Invalid username and password combination.')
	return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	'''
		This function facilitates registration of new users. 
			-When the sign up form is submitted and validated, 
			 a new user is added to the database
	'''
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('auth.login'))
	return render_template('auth/signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	'''
		The logout() function calls the Flask Login function logout_user() that
			removes and resets user session. 
		The logout is completed with a flash message that confirms the action
			and redirect to the home page.
	'''
	logout_user()
	#flash('You have been logged out.')
	return redirect(url_for('main.index'))

