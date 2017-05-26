from flask import Flask
from .conf import config
from .main import main as main_blueprint
from .ticket_viewer import ticket_viewer as ticket_viewer_blueprint


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)
    app.register_blueprint(ticket_viewer_blueprint, url_prefix='/tickets')
    return app
