FROM networktocode/nautobot:latest AS build
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
USER root
RUN apt-get -y update \
    && apt-get -y install build-essential git iputils-ping nmap vim
USER nautobot
CMD ["sleep", "3600"]
