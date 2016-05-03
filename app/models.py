from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	email_address = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	@property 
	def password(self):
		'''
		'''
		raise AttributeError('password cannot be read (write-only attribute)')

	@password.setter
	def password(self, password):
		'''
		'''
		self.password_hash = generate_password_hash(password)


	def verify_password(self, password):
		'''
		'''
		return check_password_hash(self.password_hash, password)

	@login_manager.user_loader
	def load_user(user_id):
		'''	
			Is a Flask-Login callback function.
			It loads a user, given the identifier.
		'''
		return User.query.get(int(user_id))

	