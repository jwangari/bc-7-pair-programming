import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
	'''
		The setUp() and tearDown() methods run before and after each test
		Methods that begin with test_ are executed as tests
	'''
	def setUp(self):
		'''
			-It creates an application cofigured for testing and activates its context.
			-It creates a new database that the test can use when necessary.
		'''
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		'''
			This method removes the database and application context created.
		'''
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_app_exists(self):
		'''
			Ensures that the application instance exists
		'''
		self.assertFalse(current_app is None)

	def test_app_is_testing(self):
		'''
			Ensures that the application is running the test configuration
		'''
		self.assertTrue(current_app.config['TESTING'])