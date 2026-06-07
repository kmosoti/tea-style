---
id: doctrine:repo:systems-should-tell-on-themselves
title: Systems Should Tell on Themselves
type: doctrine
domain: repo-wide
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Good systems reduce guessing by exposing state, capturing evidence, and making failure modes visible.
concepts:
  - evidence
  - operability
  - state exposure
  - failure modes
  - context regression
edges:
  supports:
    - doctrine:repo:engineering-control-spine
  refines:
    - doctrine:repo:tea-style-doctrine
  contradicts:
    - antipattern:hidden-operational-context
    - antipattern:vanity-metrics
origin:
  author: human
  review: manual
---

# Systems Should Tell on Themselves

## Purpose
Define the root operating philosophy behind the doctrine graph.

## Core claim
Good systems reduce guessing by exposing state, capturing evidence, and making failure modes visible.

## Definitions
- **Tell on themselves**: expose enough state, context, and evidence that future operators do not need hidden author knowledge.
- **Evidence**: structured proof that a claim, change, validation, or failure actually happened.
- **Hidden context**: operational knowledge that exists only in a person's memory or an unstated workflow.

## Architecture / Mechanics
Use this doctrine when reviewing any system that can mutate, diagnose, report, or influence operational decisions.

The system should answer:
- what happened
- why it happened
- what state it observed
- what it changed
- what evidence supports the outcome
- what a future operator should do next

## Patterns
- expose state directly
- capture evidence as data
- keep mutation visible
- make boundaries obvious
- record provenance
- write reports from structured results

## Anti-patterns
- hidden operational context
- vanity metrics without decision value
- scripts only the original author can explain
- agents hallucinating operational state
- prose-only reports that cannot be inspected mechanically

## Related pages
- [engineering-control-spine.md](engineering-control-spine.md)
- [docs/standards/graph-knowledge-base-standard.md](../standards/graph-knowledge-base-standard.md)
- [kb/notes/evidence/systems-should-tell-on-themselves.md](../../kb/notes/evidence/systems-should-tell-on-themselves.md)
