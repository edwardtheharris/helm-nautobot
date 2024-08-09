#!/bin/bash

set -x

rm -rfv /opt/nautobot

mkdir -pv /opt/nautobot

chown -v nautobot:nautobot /opt/nautobot

apk add --no-cache sudo

sudo -u nautobot python -m venv /opt/nautobot

sudo -u nautobot /opt/nautobot/bin/pip install -U pip

sudo -u nautobot /opt/nautobot/bin/pip install -r /opt/.nautobot/reqs

cat /opt/.nautobot/.bashrc > /opt/nautobot/.bashrc

chown -v nautobot:nautobot /opt/nautobot/.bashrc

NAUTOBOT_ROOT=/opt/nautobot
export NAUTOBOT_ROOT

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server init

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server migrate

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server createsuperuser --email "${NAUTOBOT_SUPERUSER_EMAIL}" --username "${NAUTOBOT_SUPERUSER_USERNAME}" --noinput

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server collectstatic
