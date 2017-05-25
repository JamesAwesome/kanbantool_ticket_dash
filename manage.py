#!/usr/bin/env python3

import os
from flask_script import Manager, Shell
from kanbantool_ticket_dash import create_app

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()
