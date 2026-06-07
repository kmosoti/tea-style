---
id: note:evidence:evidence-over-vanity-metrics
title: Evidence Over Vanity Metrics
type: note
domain: observability
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Prefer evidence that changes decisions over metrics that only make activity visible.
concepts:
  - evidence
  - observability
  - metrics
edges:
  supports:
    - note:evidence:systems-should-tell-on-themselves
  contradicts:
    - antipattern:vanity-metrics
origin:
  author: human
  review: manual
---

# Evidence Over Vanity Metrics

## Core claim
Evidence beats vanity metrics.

## Why it matters
Counting PRs, tokens, reports, runs, or dashboards does not prove the system became safer, clearer, or easier to operate.

## Use this when
Use this when selecting metrics, evaluating automation, reviewing agent output, or deciding whether a report is useful.

## Failure smell
A report celebrates activity but cannot answer what changed, what failed, or what decision should be made.

## Related doctrine
- [Systems Should Tell on Themselves](../../../docs/doctrines/systems-should-tell-on-themselves.md)
- [Observability Principles](../../../domains/observability/principles.md)
