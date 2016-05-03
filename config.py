import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = 'True'
	SQLALCHEMY_TRACK_MODIFICATIONS  = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqllite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True 
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqllite:///' + os.path.join(basedir, 'data-dev.sqlite')

#class ProductionConfig(Config):

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'default': DevelopmentConfig
}