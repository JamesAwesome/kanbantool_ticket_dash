import os, json

from kanbantool_ticket_dash import utils
from . import ticket_viewer
from flask import current_app, render_template, request
import requests

@ticket_viewer.route('/')
def index():
    return render_template('ticket_viewer/index.html', tickets=utils.fetch_tickets())
