FROM python:3.11-alpine AS build
ARG USER=nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="${USER}"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1.rc30"
COPY container/${USER}.entrypoint.sh /bin/entrypoint.sh
COPY container/reqs /opt/${USER}/reqs
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
    sudo \
    vim \
    xmlsec-dev \
    zlib-dev \
    && chmod +x /bin/entrypoint.sh \
    && groupadd ${USER} \
    && useradd -s /bin/bash -m -d /opt/${USER} -g ${USER} ${USER}
CMD ["/bin/entrypoint.sh", "${USER}"]
