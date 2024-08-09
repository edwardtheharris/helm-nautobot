#!/bin/bash

NAUTOBOT_ALLOWED_HOSTS="*"
NAUTOBOT_DB_ENGINE='django.db.backends.postgresql'
NAUTOBOT_DB_HOST='postgresql.postgresql.svc.cluster.local'
NAUTOBOT_DB_NAME='nautobot'
NAUTOBOT_DB_PORT='5432'
NAUTOBOT_DB_USER='nautobot'
NAUTOBOT_ROOT=/opt/nautobot
PATH="/opt/nautobot/bin:$PATH"

export NAUTOBOT_ALLOWED_HOSTS
export NAUTOBOT_DB_ENGINE
export NAUTOBOT_DB_HOST
export NAUTOBOT_DB_NAME
export NAUTOBOT_DB_PORT
export NAUTOBOT_DB_USER
export NAUTOBOT_ROOT
export PATH
