ARG PYTHON_VERSION='3.12'
FROM python:${PYTHON_VERSION}-alpine AS build
ARG VERSION
ARG USER=nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="${USER}"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL org.opencontainers.image.description="Runs ${USER} for nautobot on Kubernetes."
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="${VERSION}"
RUN apk add --no-cache \
    alpine-sdk \
    bash \
    git \
    iputils-ping \
    libxml2-dev \
    jpeg-dev \
    mailcap \
    nmap \
    pkgconfig \
    python3-dev \
    shadow \
    sudo \
    vim \
    xmlsec-dev \
    zlib-dev \
    && groupadd ${USER} \
    && useradd -s /bin/bash -m -d /opt/${USER} -g ${USER} ${USER}
CMD ["tail", "-f", "/dev/null"]
