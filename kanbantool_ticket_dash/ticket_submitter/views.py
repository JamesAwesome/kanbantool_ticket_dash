import os, json

from kanbantool_ticket_dash import utils
from . import ticket_submitter
from .form import TicketSubmitForm
from flask import current_app, render_template


@ticket_submitter.route('/', methods=['GET', 'POST'])
def index():
    ticket_form = TicketSubmitForm()

    if ticket_form.validate_on_submit():
        title        = ticket_form.title.data
        submitted_by = ticket_form.submitted_by.data
        due_date     = ticket_form.due_date.data
        description  = ticket_form.description.data

        ticket = utils.create_ticket(title, description, submitted_by, due_date)

        if current_app.config['SLACK_TOKEN']:
            sc = utils.make_slackclient()
            utils.post_slack_message(sc,
                'Ticket: #{}, "{}" | Has been Submitted by {}'.format(
                    ticket['task']['id'],
                    title,
                    submitted_by
                )
            )

        return render_template(
            'ticket_submitter/thank_you.html',
            form=ticket_form,
            ticket=ticket,
        )

    return render_template(
        'ticket_submitter/index.html',
        form=ticket_form,
    )
