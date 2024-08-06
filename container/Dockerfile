FROM python:3.11-alpine AS build
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="build"
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
    zlib-dev


FROM python:3.11-alpine AS nautobot
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="celery"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1.rc27"
COPY --from=build /usr/sbin /usr/sbin
RUN useradd -m -d /opt/nautobot -s /bin/bash -g nautobot nautobot \
    && chmod +x /bin/entrypoint.sh
USER nautobot
RUN python -m venv /opt/nautobot \
    && /opt/nautobot/bin/pip install --no-cache-dir -U --pre \
    loguru \
    --no-binary=lxml \
    --no-binary=xmlsec \
    nautobot[sso] \
    pip \
    wheel
CMD ["/bin/entrypoint.sh"]

FROM python:3.11-alpine AS celery
LABEL io.ghcr.edwardtheharris.helm-nautobot.editor="Xander Harris"
LABEL io.ghcr.edwardtheharris.helm-nautobot.name="celery"
LABEL org.opencontainers.image.source="https://github.com/edwardtheharris/helm-nautobot"
LABEL io.ghcr.edwardtheharris.helm-nautobot.version="0.0.1.rc27"
COPY --from=build /bin/bash /bin/bash
COPY --from=build /usr/sbin/useradd /usr/sbin/useradd
COPY --from=build /usr/sbin/groupadd /usr/sbin/groupadd
COPY --from=build /usr/lib/libbsd.so.0 /usr/lib/libbsd.so.0
COPY --from=build /usr/lib/libmd.so.0 /usr/lib/libmd.so.0
COPY container/entrypoint.sh /bin/entrypoint.sh
RUN groupadd celery \
    && useradd -m -d /opt/celery -s /bin/bash -g celery celery \
    && chmod +x /bin/entrypoint.sh
USER celery
COPY container/reqs /opt/celery/reqs
RUN python -m venv --system-site-packages --symlinks --upgrade --upgrade-deps /opt/celery \
    && /opt/celery/bin/pip install --no-cache-dir -U --pre pip
WORKDIR /opt/celery
RUN bin/pip install --no-cache-dir -U -r reqs \
    && rm -rf reqs
CMD ["/bin/entrypoint.sh"]
