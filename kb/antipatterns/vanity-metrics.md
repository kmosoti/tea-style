---
id: antipattern:vanity-metrics
title: Vanity Metrics
type: antipattern
domain: observability
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Metrics that show activity without improving decisions, diagnosis, or safety.
concepts:
  - evidence
  - metrics
edges:
  contradicts:
    - note:evidence:evidence-over-vanity-metrics
origin:
  author: human
  review: manual
---

# Vanity Metrics

## Failure mode
A metric demonstrates activity but does not improve decision quality or operational clarity.

## Detection
The metric cannot answer what changed, what failed, what risk moved, or what action should happen next.
