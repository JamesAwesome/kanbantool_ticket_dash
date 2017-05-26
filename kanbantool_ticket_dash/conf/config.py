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

config = {
    'default': Config,
}
