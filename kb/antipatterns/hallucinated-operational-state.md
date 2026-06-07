---
id: antipattern:hallucinated-operational-state
title: Hallucinated Operational State
type: antipattern
domain: observability
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  A human, agent, or tool claims system state without evidence from authoritative sources.
concepts:
  - observability
  - explicit-state
  - evidence
edges:
  contradicts:
    - note:observability:operators-should-not-hallucinate-system-state
origin:
  author: human
  review: manual
---

# Hallucinated Operational State

## Failure mode
A human, agent, or tool claims current system state without evidence from authoritative sources.

## Detection
Status is asserted without source, timestamp, check result, or confidence boundary.
