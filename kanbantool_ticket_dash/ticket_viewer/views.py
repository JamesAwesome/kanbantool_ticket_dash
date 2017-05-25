import os

from . import ticket_viewer
from flask import json, jsonify, current_app, render_template, request

@ticket_viewer.route('/')
def index():
    return render_template('ticket_viewer/index.html', kanbantool_api_key=current_app.config['KANBANTOOL_API_KEY'])
