#!/bin/bash

rm -rfv /opt/celery
mkdir -pv /opt/celery
chown -v celery:celery /opt/celery

apk add --no-cache sudo

sudo -u celery python -m venv /opt/celery

sudo -u celery /opt/celery/bin/pip install -U pip

sudo -u celery /opt/celery/bin/pip install -r /opt/.celery/reqs

cat /opt/.celery/.bashrc > /opt/celery/.bashrc

chown -v celery:celery /opt/celery/.bashrc

sudo -E -u celery /opt/celery/bin/nautobot-server init
