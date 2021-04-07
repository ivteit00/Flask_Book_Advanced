# Standard libary imports
from datetime import datetime

# Third pary imports
from flask import render_template, session, redirect, url_for

# Local application imports
from . import main


@main.route('/', methods=['GET', 'POST'])
def index() -> 'html':
    """Log-In-viewfunction"""
    from .forms import LoginForm

    return render_template('login.html', form=LoginForm())


# MA-home-viewfunction
@main.route('/home')
def ma_home():
    return '<h1>Mitarbeiter Home View'


# MA-statistic-viewfunction


# MA-vacation-viewfunction


# SU-home-viewfunction


# SU-applications-viewfunction


# HR-home-viewfunction
