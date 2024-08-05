FROM python:3.11-alpine AS nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
USER root
COPY container/entrypoint.sh /bin/entrypoint.sh
RUN apk add --no-cache \
    alpine-sdk \
    bash \
    git \
    iputils-ping \
    libxml2-dev \
    jpeg-dev \
    nmap \
    pkgconfig \
    python3-dev \
    shadow \
    vim \
    xmlsec-dev \
    zlib-dev \
    && groupadd nautobot \
    && useradd -m -d /opt/nautobot -s /bin/bash -g nautobot nautobot \
    && chmod +x /bin/entrypoint.sh
USER nautobot
RUN python -m venv /opt/nautobot \
    && /opt/nautobot/bin/pip install -U --pre nautobot pip wheel
CMD ["/bin/entrypoint.sh"]
