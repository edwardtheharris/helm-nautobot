FROM networktocode/nautobot:latest AS build
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="nautobot"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1"
USER root
RUN apt-get -y update \
    && apt-get -y install git iputils-ping nmap vim \
    && pip install -U loguru nautobot pip --no-binary=pyuwsgi
COPY --chown=nautobot:nautobot nautobot_config.py /opt/nautobot/nautobot_config.py
USER nautobot
CMD ["sleep", "3600"]
