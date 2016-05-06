import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = 'True'
	SQLALCHEMY_TRACK_MODIFICATIONS  = True
	PAIRPROGRAM_MAIL_SUBJECT_PREFIX = '[pairprogram]'
	PAIRPROGRAM_MAIL_SENDER = 'Admin <warugujoy@gmail.com>'
	PAIRPROGRAM_ADMIN = os.environ.get('PAIRPROGRAM_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'warugujoy@gmail.com'
	MAIL_PASSWORD = 'spdwndzzvvgwtucr'
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True 
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}