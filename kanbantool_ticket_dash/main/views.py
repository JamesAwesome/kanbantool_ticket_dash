import os

from . import main

@main.route('/')
def index():
    return 'Hello World'
