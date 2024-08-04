FROM python:alpine AS nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
USER root
RUN apk add alpine-sdk git iputils-ping jpeg-dev nmap python3-dev vim zlib-dev \
    && python -m venv /opt/nautobot \
    && /opt/nautobot/bin/pip install -U pip \
    && /opt/nautobot/bin/pip install nautobot
COPY nautobot_config.py /opt/nautobot/nautobot_config.py
USER nautobot
CMD ["sleep", "3600"]

FROM python:alpine AS celery
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="celery"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
RUN apk add alpine-sdk bash git vim \
    && python -m venv /opt/celery \
    && /opt/celery/bin/pip install -U celery pip \
    && ln -sfv /opt/celery/bin/celery /usr/bin/celery
CMD ["sleep", "3600"]
