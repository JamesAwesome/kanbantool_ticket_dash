import os, json

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

        return render_template(
            'ticket_submitter/thank_you.html',
            form=ticket_form
        )

    return render_template(
        'ticket_submitter/index.html',
        form=ticket_form,
    )
