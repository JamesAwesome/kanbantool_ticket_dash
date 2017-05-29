import os, json

from . import ticket_submitter
from flask import current_app, render_template

@ticket_submitter.route('/')
def index():
    return "Hello World!"
