import unittest import Testcase
from app.models import User

class UserModelTestCase(Testcase):
	def test_password_setter(self):
		u = User(password='pas123')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password='pas123')
		with self.assertRaises(AttributError):
			u.password

	def test_password_verifiation(self):
		u = User(password='pas123')
		self.assertTrue(u.verify_password('pas123'))
		self.assertFalse(u.verify_password('pas12'))

	def test_password_salts_are_random(self):
		u = User(password='pas123')
		u2 = User(password='pas123')
		self.assertTrue(u.password_hash != u2.password_hash)


