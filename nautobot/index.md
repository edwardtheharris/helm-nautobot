---
abstract: Nautobot chart, values and templates.
authors: Xander Harris
date: 2024-04-28
title: Nautobot Chart and Templates
---

## Usage

Deploy this chart using Helm. The current iteration expects a PostgreSQL
instance to be running in the `postgres` namespace and a Redis instance to be
running in the `redis` namespace.

### Chart

```{autoyaml} nautobot/Chart.yaml
```

#### Values

```{autoyaml} nautobot/values.yaml
```
