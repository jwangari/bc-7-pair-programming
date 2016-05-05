from datetime import datetime
from flask import render_template, session, redirect, url_for, request, Response, jsonify
from flask.ext.login import current_user, login_required
from . import main
from .. import db
from..models import User, ProgramSession
from . forms import NewSessionForm
from firebase import firebase
from app.email import send_email

session_url = ""

@main.route('/', methods=['GET', 'POST'])
def start():
	
	return render_template('start.html')

@main.route('/index', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

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
		return redirect(url_for('main.invite'))
	return render_template('main/new_session.html', form=form)

@main.route('/invite', methods=['GET', 'POST'])
@login_required
def invite():
    users = User.query.all()
    if request.method == 'POST':
        for user in users:
            if str(user.username+' ') == str(request.form.get('usernames')):
                print user.username
                session_link = request.form.get('session_link')
                send_email(current_user.email, user.email, "Invitation", 'mail/invite', user=user,  current_user=current_user, session_link=session_link)
                flash('An invitation has been sent to user.')
                print str(session_link)
    return render_template('main/home.html', users=users)

@main.route('/sessions', methods=['GET', 'POST'])
@login_required
def my_session():
        firebase_ = firebase.FirebaseApplication('https://pairprogram.firebaseio.com/')
        results = firebase_.get('https://pairprogram.firebaseio.com/', None)
        sess_hash = []
        for item in results:
            for first_name in results[item]:
                if str(current_user.username) == str(results[item][first_name].get('username')).strip():
                    # print results[item][first_name].get('username')
                    sess_hash.append(str(results[item][first_name].get('session')))
        return render_template('main/my_session.html', sess_hash=sess_hash)

@main.route('/edit/<hashed>')
def edit(hashed):
    global session_url
    session_url = "http://127.0.0.1:5000/invite#"+hashed
    return redirect(session_url)

@main.route('/delete/<hashed>')
def delete(hashed):
    firebase_ = firebase.FirebaseApplication('https://pairprogram.firebaseio.com/')
    results = firebase_.get('https://pairprogram.firebaseio.com/', None)
    for item in results:
        for n in results[item]:
            if str(current_user.username) == str(results[item][n].get('username')).strip():
                print results[item][n].get('session')
                print "Hashed -->"+hashed
                if results[item][n].get('session') == hashed:
                    print True
                    firebase_.delete(current_user.username, '1')
    return redirect(url_for('main.my_session'))


@main.route('/chat')
@login_required
def chat():
    return render_template('main/chat.html')

@main.route('/chat_session')
@login_required
def chat_session():
    return render_template('main/chat_session.html')
