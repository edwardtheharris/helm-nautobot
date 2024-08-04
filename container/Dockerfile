FROM python:alpine AS nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
USER root
RUN apk add --no-cache alpine-sdk git iputils-ping jpeg-dev nmap python3-dev shadow vim zlib-dev \
    && python -m venv /opt/nautobot \
    && /opt/nautobot/bin/pip install --no-cache-dir -U pip \
    && /opt/nautobot/bin/pip install --no-cache-dir nautobot \
    && useradd -m -d /opt/nautobot -s /bin/bash -g nautobot nautobot
COPY --chown=nautobot:nautobot nautobot_config.py /opt/nautobot/nautobot_config.py
USER nautobot
CMD ["sleep", "3600"]
