---
abstract: Continuous Integration, Deployment, and Delivery usage guide.
authors:
    - name: Xander Harris
      email: xandertheharris@gmail.com
date: 2024-08-11
title: CI/CD guide
---

Or something like it.

## Dependabot

```{autoyaml} .github/dependabot.yml
```

## GitHub Actions Workflows

This repository runs the following GitHub Actions

### CodeQL

[![CodeQL](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/codeql.yml/badge.svg)](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/codeql.yml)

```{autoyaml} .github/workflows/codeql.yml
```

### Documentation

[![Documentation](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/documentation.yml/badge.svg)](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/documentation.yml)

This job checks the documentation markdown for errors, posts the results
to the associated PR, builds the documentation site, and publishes the site
to the `github-pages` environment.

```{autoyaml} .github/workflows/documentation.yml
```

### Helm

[![Helm Tests](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/helm.yml/badge.svg)](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/helm.yml)

```{autoyaml} .github/workflows/helm.yml
```

### OSSAR

[![OSSAR](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/ossar.yml/badge.svg)](https://github.com/edwardtheharris/helm-nautobot/actions/workflows/ossar.yml)

```{autoyaml} .github/workflows/ossar.yml
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com
```
