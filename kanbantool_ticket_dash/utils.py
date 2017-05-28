import os, json

import arrow
import requests
from flask import current_app

from functools import lru_cache

def fetch_tickets():
    r = requests.get(
            'https://{}.kanbantool.com/api/v1/boards/{}/tasks.json'.format(
                current_app.config['KANBANTOOL_ORG'],
                current_app.config['KANBANTOOL_BOARD_ID']
            ),
            params={
                'api_token': current_app.config['KANBANTOOL_API_KEY'],
                'swimlane_id': current_app.config['KANBANTOOL_TICKET_SWIMLANE_ID'],
            }
        )

    tickets = json.loads(r.text)

    for ticket in tickets:
        ticket['task']['created_at'] = arrow.get(ticket['task']['created_at'])

    return tickets


@lru_cache(maxsize=100)
def fetch_board_desc():
    r = requests.get(
            'https://{}.kanbantool.com/api/v1/boards/{}.json'.format(
                current_app.config['KANBANTOOL_ORG'],
                current_app.config['KANBANTOOL_BOARD_ID'],
            ),
            params={
                'api_token': current_app.config['KANBANTOOL_API_KEY'],
            }
        )

    return json.loads(r.text)


@lru_cache(maxsize=100)
def create_workflow_mapper():
    board_desc = fetch_board_desc()
    workflow_stages = board_desc['board']['workflow_stages']
    return { w['id']: w['name'] for w in workflow_stages }


def sort_tickets(tickets, workflow_mapper, ticket_sorter):
    unstarted = find_and_sort_unstarted_tickets(tickets, workflow_mapper, ticket_sorter)
    wip       = find_and_sort_wip(tickets, workflow_mapper, ticket_sorter)
    done      = find_and_sort_done_tickets(tickets, workflow_mapper, ticket_sorter)

    return {
        'unstarted': unstarted,
        'wip': wip,
        'done': done
    }


def all_work_lanes():
    return current_app.config['KANBANTOOL_UNSTARTED_LANES'] + \
        current_app.config['KANBANTOOL_WIP_LANES'] + \
        current_app.config['KANBANTOOL_DONE_LANES']


def make_ticket_sorter(workflow_mapper):
    def wrapped(ticket):
        workflow_stage = workflow_mapper[ticket['task']['workflow_stage_id']]
        return all_work_lanes().index(workflow_stage), ticket['task']['id']
    return wrapped


def find_and_sort_unstarted_tickets(tickets, workflow_mapper, ticket_sorter):
    unstarted_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_UNSTARTED_LANES'], tickets)
    return sorted(unstarted_tickets, key=ticket_sorter)


def find_and_sort_wip(tickets, workflow_mapper, ticket_sorter):
    wip_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_WIP_LANES'], tickets)
    return sorted(wip_tickets, key=ticket_sorter)


def find_and_sort_done_tickets(tickets, workflow_mapper, ticket_sorter):
    done_tickets = filter(lambda t: workflow_mapper[t['task']['workflow_stage_id']] in current_app.config['KANBANTOOL_DONE_LANES'], tickets)
    return sorted(done_tickets, key=ticket_sorter)
