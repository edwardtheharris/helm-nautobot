#!/bin/bash

chown -v celery:celery /opt/celery

apk add --no-cache sudo

sudo -u celery python -m venv /opt/celery

sudo -u celery /opt/celery/bin/pip install -U pip

sudo -u celery /opt/celery/bin/pip install -r /opt/celery/.celery/reqs
