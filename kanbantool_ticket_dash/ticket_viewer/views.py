import os, json

from . import ticket_viewer
from flask import current_app, render_template, request
import requests


def fetch_tickets():
    r = requests.get(
            'https://grovo.kanbantool.com/api/v1/boards/316743/tasks.json',
            params={'api_token': current_app.config['KANBANTOOL_API_KEY'], 'swimlane_id': '750005' }
        )

    return json.loads(r.text)

@ticket_viewer.route('/')
def index():
    return render_template('ticket_viewer/index.html', tickets=json.dumps(fetch_tickets(), indent=4, sort_keys=True))
