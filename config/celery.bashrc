#!/bin/bash

HOME=/opt/celery
NAUTOBOT_ROOT=/opt/celery
PATH="/opt/celery/bin:$PATH"

export HOME
export NAUTOBOT_ROOT
export PATH

/usr/local/bin/python -m venv /opt/celery/
/opt/celery/bin/pip install -r /opt/celery/.celery/reqs
/opt/celery/bin/pip install -U pip
/opt/celery/bin/nautobot-server celery worker --loglevel DEBUG
