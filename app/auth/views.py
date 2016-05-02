from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from auth/forms import LogInForm, SignUpForm
from . import auth

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
			return redirect(url_for('main.index'))
		flash('Invalid username and password combination.')
	return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('main.index'))
	return render_template('signin.html')

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
	flash('You have been logged out.')
	return redirect(url_for('main.index'))

