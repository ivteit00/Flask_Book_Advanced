from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email

# Name Form


class NameForm(FlaskFrom):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')

# EmailForm


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[Email(), Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')


# LoginForm
class LoginForm(FlaskForm):
    pass


# WorktimeForm
class WortimeForm(FlaskFrom):
    pass


# VacationForm
class VacationForm(FlaskForm):
    pass


# AcceptRejectForm
class AcceptRejectForm(FlaskForm):
    pass
