import os

from . import main
from flask import json, jsonify, current_app, render_template, request

@main.route('/')
def index():
    return render_template('main/index.html', iotd=current_app.config['IOTD'], motd=current_app.config['MOTD'])
