from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email

# Name Form


class NameForm(Form):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')

# EmailForm


class EmailForm(Form):
    email = StringField('Email', validators=[Email(), Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')


# LoginForm
class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')


# WorktimeForm
class WortimeForm(Form):
    pass


# VacationForm
class VacationForm(Form):
    pass


# AcceptRejectForm
class AcceptRejectForm(Form):
    pass
