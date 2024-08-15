---
abstract: >-
    How to build the containers required for this project.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2024-08-06
title: Nautobot Containers
---

This project uses two containers, one for Nautobot and the other for Celery.

To build the nautobot container you run the build command below.

```{code-block} shell
:caption: build nautobot

VERSION=0.0.2

export VERSION

docker build --build-arg VERSION="${VERSION}" \
  --build-arg PYTHON_VERSION='3.12' \
  -t ghcr.io/edwardtheharris/helm-nautobot/nautobot:${VERSION} \
  --progress plain --push -f container/Dockerfile .
```

The Celery container requires the `celery` user, which is passed in as a build
argument as shown below.

```{code-block} shell
:caption: build celery

VERSION=0.0.2

export VERSION

docker build --build-arg PYTHON_VERSION='3.12' --build-arg USER=celery \
    --build-arg="${VERSION}" \
    -t ghcr.io/edwardtheharris/helm-nautobot/celery:${VERSION} \
    --progress plain --push -f container/Dockerfile .
```
