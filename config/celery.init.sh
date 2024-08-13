#!/bin/bash

set -x

cat /opt/.celery/resolv.conf > /etc/resolv.conf

rm -rfv /opt/celery

mkdir -pv /opt/celery

chown -Rv celery:celery /opt/celery

apk add --no-cache sudo

sudo -u celery python -m venv /opt/celery

sudo -u celery /opt/celery/bin/pip install --no-cache-dir -U pip -v

sudo -u celery /opt/celery/bin/pip install --no-cache-dir -r /opt/.celery/reqs

cat /opt/.celery/.bashrc > /opt/celery/.bashrc

chown -v celery:celery /opt/celery/.bashrc

NAUTOBOT_ROOT=/opt/celery
export NAUTOBOT_ROOT

sudo -E -u celery /opt/celery/bin/nautobot-server init

exit 0
