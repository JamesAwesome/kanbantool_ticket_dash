from kanbantool_ticket_dash import create_app, utils


def test_all_work_lanes(app):
    assert(utils.all_work_lanes() == ['Backlog', 'Ready', 'Started', 'In Dev', 'In Prod', 'Done'])
