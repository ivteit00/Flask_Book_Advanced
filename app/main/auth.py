# Standard libary imports
from datetime import datetime

# Third pary imports
from flask import render_template, session, redirect, url_for, request

# Local application imports
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """Log-In-viewfunction"""
    if request.method == 'POST':
        print(request.form.get('email'))

    return render_template('login.html')
