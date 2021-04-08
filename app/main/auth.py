# Standard libary imports
from datetime import datetime

# Third pary imports
from flask import render_template, session, redirect, url_for, request

# Local application imports
from . import main


def valid_login(email: str, password: str) -> bool:
    """Checks if the email and password received in the form match with a user in the database"""
    from .. import db
    from ..models import User, Role


@main.route('/', methods=['GET', 'POST'])
def index():
    """Log-In-viewfunction"""
    if request.method == 'POST':
        print(request.form.get('email'))
        if valid_login(email=request.form.get('email'), password=request.form.get('password')):
            return redirect(url_for('main.index'))

    return render_template('login.html')
