from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response, jsonify
from flask.ext.login import current_user, login_required
from . import main
from .. import db
from..models import User, ProgramSession
from . forms import NewSessionForm
from firebase import firebase


@main.route('/', methods=['GET', 'POST'])
def index():
	
	return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('main/home.html')

@main.route('/new_session', methods=['GET', 'POST'])
def new_session():
	''' This function facilitates the creation of new pair programming sessions '''
	form = NewSessionForm()
	if form.validate_on_submit():
		sess = ProgramSession(session_name=form.session_name.data, program_lang=form.program_lang.data)
		if current_user.id is not None:
			user = User.query.get(current_user.id)
			user.sessions.append(sess)
			db.session.add(user)
			db.session.commit()
		return redirect(url_for('main.home'))
	return render_template('main/new_session.html', form=form)

@main.route('/chat')
@login_required
def chat():
    return render_template('main/chat.html')

@main.route('/chat_session')
@login_required
def chat_session():
    return render_template('main/chat_session.html')












