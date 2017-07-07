import os
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

class Config:
    VERSION = '0.0.1'
    DEBUG = True
    DEFAULT = True
    KANBANTOOL_API_KEY            = os.environ.get('KANBANTOOL_API_KEY')
    KANBANTOOL_ORG                = os.environ.get('KANBANTOOL_ORG')
    KANBANTOOL_TICKET_SWIMLANE_ID = os.environ.get('KANBANTOOL_TICKET_SWIMLANE_ID')
    KANBANTOOL_BOARD_ID           = os.environ.get('KANBANTOOL_BOARD_ID')
    KANBANTOOL_UNSTARTED_LANES    = os.environ.get('KANBANTOOL_UNSTARTED_LANES') or ['Backlog', 'Ready']
    KANBANTOOL_WIP_LANES          = os.environ.get('KANBANTOOL_WIP_LANES') or ['Started', 'In Dev', 'In Prod']
    KANBANTOOL_DONE_LANES         = os.environ.get('KANBANTOOL_DONE_LANES') or ['Done']
    SECRET_KEY                    = os.environ.get('CSRF_SECRET_KEY')
    SLACK_TOKEN                   = os.environ.get('SLACK_TOKEN') or False
    SLACK_CHANNEL                 = os.environ.get('SLACK_CHANNEL') or '#general'
    SLACK_NOTIFY                  = os.environ.get('SLACK_NOTIFY') or False
    IOTD                          = os.environ.get('IOTD') or False
    MOTD                          = os.environ.get('MOTD') or False


class TestingConfig(Config):
    TESTING = True
    KANBANTOOL_UNSTARTED_LANES    = ['Backlog', 'Ready']
    KANBANTOOL_WIP_LANES          = ['Started', 'In Dev', 'In Prod']
    KANBANTOOL_DONE_LANES         = ['Done']


config = {
    'default': Config,
    'testing': TestingConfig
}
