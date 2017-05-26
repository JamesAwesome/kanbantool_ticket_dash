import os, json

import requests
from flask import current_app


def fetch_tickets():
    r = requests.get(
            'https://{}.kanbantool.com/api/v1/boards/{}/tasks.json'.format(current_app.config['KANBANTOOL_ORG'], current_app.config['KANBANTOOL_BOARD_ID']),
            params={'api_token': current_app.config['KANBANTOOL_API_KEY'], 'swimlane_id': current_app.config['KANBANTOOL_TICKET_SWIMLANE_ID'] }
        )

    return json.loads(r.text)


def fetch_board_desc():
    r = requests.get(
            'https://{}.kanbantool.com/api/v1/boards/{}.json'.format(current_app.config['KANBANTOOL_ORG'], current_app.config['KANBANTOOL_BOARD_ID']),
            params={'api_token': current_app.config['KANBANTOOL_API_KEY']}
        )

    return json.loads(r.text)


def get_ticket_sort_key(ticket):
    workflow_mapper = create_workflow_mapper()
    all_lanes = current_app.config['KANBANTOOL_UNSTARTED_LANES'] + current_app.config['KANBANTOOL_WIP_LANES'] + current_app.config['KANBANTOOL_DONE_LANES']
    return all_lanes.index(workflow_mapper[ticket['task']['workflow_stage_id']])


def create_workflow_mapper():
    board_desc = fetch_board_desc()
    workflow_stages = board_desc['board']['workflow_stages']
    return { w['id']: w['name'] for w in workflow_stages }


def find_unstarted_tickets(tickets, workflow_mapper):
    unstarted_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_UNSTARTED_LANES'], tickets)
    return sorted(unstarted_tickets, key=get_ticket_sort_key)


def find_wip(tickets, workflow_mapper):
    wip_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_WIP_LANES'], tickets)
    return sorted(wip_tickets, key=get_ticket_sort_key)


def find_done_tickets(tickets, workflow_mapper):
    done_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_DONE_LANES'], tickets)
    return sorted(done_tickets, key=get_ticket_sort_key)
