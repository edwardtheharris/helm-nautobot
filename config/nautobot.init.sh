#!/bin/bash

chown -v nautobot:nautobot /opt/nautobot

apk add --no-cache sudo

sudo -u nautobot python -m venv /opt/nautobot

sudo -u nautobot /opt/nautobot/bin/pip install -U pip

sudo -u nautobot /opt/nautobot/bin/pip install -r /opt/nautobot/.nautobot/reqs

ln -sfv /opt/nautobot/.nautobot/.bashrc /opt/nautobot/.bashrc
ln -sfv /opt/nautobot/.nautobot/nautobot_config.py /opt/nautobot/nautobot_config.py

NAUTOBOT_ROOT=/opt/nautobot
export NAUTOBOT_ROOT

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server --config /opt/nautobot/nautobot_config.py migrate

sudo -E -u nautobot /opt/nautobot/bin/nautobot-server --config /opt/nautobot/nautobot_config.py collectstatic
