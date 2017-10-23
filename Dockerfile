FROM python:3.4.3-wheezy

RUN apt-get update -y && apt-get install wget -y && apt-get clean
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb
RUN dpkg -i dumb-init_*.deb && rm -f dumb_init_*.deb

RUN mkdir -p /srv/kanbantool_ticket_dash
COPY ./ /srv/kanbantool_ticket_dash

WORKDIR /srv/kanbantool_ticket_dash

RUN pip install -e .

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["gunicorn", "--pythonpath", "/srv/kanbantool_ticket_dash/", "--bind", "0.0.0.0", "--log-level", "info", "--log-file", "-", "--access-logfile", "-", "manage:app" ]
