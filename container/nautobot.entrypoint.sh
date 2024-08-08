#!/bin/bash

USER="$1"

chown -R "$USER:$USER" "/opt/$USER"

while true; do sleep '3600'; done
