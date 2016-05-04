from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User, ProgramSession

class NewSessionForm(Form):
	session_name = StringField('Session Name:', validators=[Required(), Length(1, 64)])
	program_lang = SelectField('Language you prefer:', choices=[('js', 'javascript'),
                                                             ('erb', 'ruby'), ('java', 'java'), ('cpp', 'C++'),
                                                             ('py', 'Python'), ('text', 'Plain Text')])
	submit = SubmitField('Create Session')