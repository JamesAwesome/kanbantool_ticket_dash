from flask import Blueprint

ticket_submitter = Blueprint('ticket_submitter', __name__, template_folder='templates')

from . import views
