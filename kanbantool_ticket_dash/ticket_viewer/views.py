import os

from . import ticket_viewer
from flask import json, jsonify, current_app, render_template, request

@ticket_viewer.route('/')
def index():
    return 'This is the ticket viewer API Key: {}'.format(current_app.config['KANBANTOOL_API_KEY'])
