FROM python:wheezy

RUN mkdir -p /srv/kanbantool_ticket_dash

COPY ./ /srv/kanbantool_ticket_dash

WORKDIR /srv/kanbantool_ticket_dash

RUN pip install -e .

CMD gunicorn --pythonpath /srv/kanbantool_ticket_dash/ --bind 0.0.0.0 --log-level info --log-file - --access-logfile - manage:app
