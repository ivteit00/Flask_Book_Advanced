# Standard libary imports
from datetime import datetime
from functools import wraps

# Third pary imports
from flask import render_template, session, redirect, url_for, request

# Local application imports
from . import main


# MA-home-viewfunction
@main.route('/home')
def ma_home():
    return '<h1>Mitarbeiter Home View'


# MA-statistic-viewfunction


# MA-vacation-viewfunction


# SU-home-viewfunction


# SU-applications-viewfunction


# HR-home-viewfunction
