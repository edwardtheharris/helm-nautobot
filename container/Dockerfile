FROM python:3.11-alpine AS build
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1.rc27"
USER root
COPY container/entrypoint.sh /bin/entrypoint.sh
COPY container/reqs /opt/reqs
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
    && chmod +x /bin/entrypoint.sh
