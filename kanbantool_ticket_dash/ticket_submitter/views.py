import os, json

from . import ticket_submitter
from flask import current_app, render_template

@ticket_submitter.route('/')
def index():
    return render_template('ticket_submitter/index.html')
