#!/bin/bash

chown -v nautobot:nautobot /opt/nautobot

apk add --no-cache sudo

sudo -u nautobot python -m venv /opt/nautobot

sudo -u nautobot /opt/nautobot/bin/pip install -U pip

sudo -u nautobot /opt/nautobot/bin/pip install -r /opt/nautobot/.nautobot/reqs
