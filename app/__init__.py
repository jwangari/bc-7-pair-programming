from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
#Initialization of the Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	'''
		Is a factory function which allows specification of 
		cofigurations before the app is created.
		It takes as an argument the name of a configuration 
		to use for the application.
		
	'''
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	bootstrap.init_app(app)
	db.init_app(app)

	from main import main as main_blueprint
	from auth import auth as auth_blueprint

	app.register_blueprint(main_blueprint)
	app.register_blueprint(auth_blueprint)
	return app
