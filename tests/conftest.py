import pytest

from kanbantool_ticket_dash import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()
