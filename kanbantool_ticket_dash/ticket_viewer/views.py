import os, json

from kanbantool_ticket_dash import utils
from . import ticket_viewer
from flask import current_app, render_template, request
import requests


@ticket_viewer.route('/')
def index():
    workflow_mapper = utils.create_workflow_mapper()
    ticket_sorter   = utils.make_ticket_sorter(workflow_mapper)
    tickets         = utils.fetch_tickets()
    sorted_tickets  = utils.sort_tickets(tickets, workflow_mapper, ticket_sorter)

    return render_template(
        'ticket_viewer/index.html',
        sorted_tickets=sorted_tickets,
        workflow_mapper=workflow_mapper
    )
