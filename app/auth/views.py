from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from auth/forms import LogInForm, SignUpForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LogInForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.keep_on.data)
			return redirect(url_for('main.index'))
	return render_template('auth/login.html')

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

#@auth.route('/logout')


