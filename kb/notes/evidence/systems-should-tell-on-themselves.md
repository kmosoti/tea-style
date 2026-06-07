---
id: note:evidence:systems-should-tell-on-themselves
title: Systems Should Tell on Themselves
type: note
domain: repo-wide
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Good systems reduce guessing by exposing state, capturing evidence, and making failure modes visible.
concepts:
  - evidence
  - operability
  - explicit-state
  - context-regression
edges:
  supports:
    - doctrine:repo:systems-should-tell-on-themselves
    - note:operability:future-operators-need-context
  refines:
    - doctrine:repo:engineering-control-spine
  contradicts:
    - antipattern:hidden-operational-context
    - antipattern:vanity-metrics
origin:
  author: human
  review: manual
---

# Systems Should Tell on Themselves

## Core claim
Good systems reduce guessing by exposing state, capturing evidence, and making failure modes visible.

## Why it matters
Systems that only work because people carry hidden context are not simple. They are undocumented risk.

## Use this when
Use this when reviewing scripts, automation, observability systems, compliance knowledge, or agent workflows that mutate or describe real systems.

## Failure smell
If future operators must ask the original author what happened, the system failed to tell on itself.

## Related doctrine
- [Systems Should Tell on Themselves](../../../docs/doctrines/systems-should-tell-on-themselves.md)
- [Engineering Control Spine](../../../docs/doctrines/engineering-control-spine.md)
