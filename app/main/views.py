from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	#session.permanent = True
	return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
def home():
    
    return render_template('main/home.html')

#@main.route('/home', methods=['GET', 'POST'])
#def new_session():
#	''' This function allows a user to create a new	pair programming session '''
#	form = 
