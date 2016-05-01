from flask.ext.login import LoginManager

#Initialization of the Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	'''
		Is a factory function which allows specification of 
		cofigurations before the app is created.
		
	'''
	app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)

	from auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='auth')
	return app
