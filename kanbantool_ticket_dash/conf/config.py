import os
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

class Config:
    VERSION = '0.0.1'
    DEBUG = True
    DEFAULT = True
    KANBANTOOL_API_KEY = os.environ.get('KANBANTOOL_API_KEY')


config = {
    'default': Config,
}
