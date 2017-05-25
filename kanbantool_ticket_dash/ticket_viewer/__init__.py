from flask import Blueprint

ticket_viewer = Blueprint('ticket_viewer', __name__, template_folder='templates')

from . import views
