#!/bin/bash

env > /opt/celery/.env

chown -R celery:celery /opt/celery

cd /opt/celery || exit

sudo -u celery python -m venv /opt/celery

