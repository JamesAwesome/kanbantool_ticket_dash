import os, json

from kanbantool_ticket_dash import utils
from . import ticket_viewer
from flask import current_app, render_template, request
import requests

@ticket_viewer.route('/')
def index():
    workflow_mapper   = utils.create_workflow_mapper()
    ticket_sorter     = utils.make_ticket_sorter(workflow_mapper)
    tickets           = utils.fetch_tickets()
    unstarted_tickets = utils.find_and_sort_unstarted_tickets(tickets, workflow_mapper, ticket_sorter)
    wip               = utils.find_and_sort_wip(tickets, workflow_mapper, ticket_sorter)
    done_tickets      = utils.find_and_sort_done_tickets(tickets, workflow_mapper, ticket_sorter)

    return render_template(
        'ticket_viewer/index.html',
        unstarted_tickets=unstarted_tickets,
        wip=wip,
        done_tickets=done_tickets,
        workflow_mapper=workflow_mapper)
