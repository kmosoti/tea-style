# Observability Principles

## Intent
This section captures how I prefer observability platforms and operational telemetry systems to be designed and evaluated.

## Core preferences
- Signal quality matters more than metric volume.
- Systems should support diagnosis, not just dashboards.
- Capacity should be treated as an operational design concern.
- Pipelines should be understandable end to end.
- Platform ownership should include maintainability and reviewability.

## What good looks like
- Useful telemetry with clear purpose
- Diagnostics that lead to action
- Capacity reasoning grounded in real system behavior
- Workflows that support triage and incident response
- Designs that scale operationally, not just theoretically

## What to avoid
- Noise without diagnostic value
- Dashboards that hide system behavior
- Poorly understood ingestion paths
- Capacity guesswork
- Operational complexity without observability into the platform itself
