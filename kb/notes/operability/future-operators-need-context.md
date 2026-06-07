---
id: note:operability:future-operators-need-context
title: Future Operators Need Context
type: note
domain: operability
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Durable systems preserve enough context for future operators to diagnose and recover without rediscovery.
concepts:
  - operability
  - provenance
  - context-regression
  - evidence
edges:
  supports:
    - doctrine:repo:systems-should-tell-on-themselves
  depends_on:
    - concept:operability
origin:
  author: human
  review: manual
---

# Future Operators Need Context

## Core claim
Future operators need context at the point of use, not in the original author's memory.

## Why it matters
The operational cost of a tool is paid during failure, handoff, and modification. Missing context compounds that cost.

## Use this when
Use this when writing reports, runbooks, generated artifacts, validation output, or workflow status records.

## Failure smell
The output says a step failed, but does not say what was checked, what state was observed, or what action is safe next.

## Related doctrine
- [Systems Should Tell on Themselves](../../../docs/doctrines/systems-should-tell-on-themselves.md)
