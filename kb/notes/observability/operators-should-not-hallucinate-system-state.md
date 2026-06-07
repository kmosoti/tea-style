---
id: note:observability:operators-should-not-hallucinate-system-state
title: Operators Should Not Hallucinate System State
type: note
domain: observability
status: active
summary: >
  Operators and agents should inspect evidence instead of guessing current system state.
concepts:
  - observability
  - explicit-state
  - evidence
  - diagnostics
edges:
  supports:
    - note:evidence:systems-should-tell-on-themselves
  contradicts:
    - antipattern:hallucinated-operational-state
origin:
  author: human
  review: manual
---

# Operators Should Not Hallucinate System State

## Core claim
Operators and agents should not hallucinate system state. They should inspect evidence.

## Why it matters
Operational guesses can trigger wrong remediations, false confidence, and wasted incident time.

## Use this when
Use this when designing dashboards, health checks, agent workflows, triage reports, or status pages.

## Failure smell
A system declares health or failure without exposing the checks, timestamps, sources, or confidence behind the claim.

## Related doctrine
- [Observability Principles](../../../domains/observability/principles.md)
- [Systems Should Tell on Themselves](../../../docs/doctrines/systems-should-tell-on-themselves.md)
