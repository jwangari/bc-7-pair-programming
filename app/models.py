from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db, login_manager

registrations = db.Table('registrations',
	db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
	db.Column('session_id', db.Integer, db.ForeignKey('sessions.id')))

class User(UserMixin, db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	sessions = db.relationship('ProgramSession',
								secondary=registrations,
								backref=db.backref('users', lazy='dynamic'),
								lazy='dynamic')

	@property 
	def password(self):
		'''
			This function raises an error if you try to read the password value.
		'''
		raise AttributeError('password cannot be read (write-only attribute)')

	@password.setter
	def password(self, password):
		'''
			Generates an password hash for a given password.
		'''
		self.password_hash = generate_password_hash(password)


	def verify_password(self, password):
		'''
			Compares the hash stored in the database with the
			password value given by user.
		'''
		return check_password_hash(self.password_hash, password)

	@login_manager.user_loader
	def load_user(user_id):
		'''	
			Is a Flask-Login callback function.
			It loads a user, given the identifier.
		'''
		return User.query.get(int(user_id))

class ProgramSession(db.Model):
	__tablename__ = 'sessions'

	id = db.Column(db.Integer, primary_key=True)
	session_name = db.Column(db.String(128), unique=True, index=True)
	session_url = db.Column(db.String(128))
	program_lang = db.Column(db.String(128))


	