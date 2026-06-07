---
id: note:context:hidden-context-is-operational-risk
title: Hidden Context Is Operational Risk
type: note
domain: operability
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Knowledge that exists only in the original author's memory makes systems fragile.
concepts:
  - operability
  - context-regression
  - provenance
edges:
  supports:
    - note:evidence:systems-should-tell-on-themselves
  contradicts:
    - antipattern:hidden-operational-context
origin:
  author: human
  review: manual
---

# Hidden Context Is Operational Risk

## Core claim
Hidden context is operational risk, even when the code appears simple.

## Why it matters
A workflow that only the original author can explain creates recovery risk, review risk, and agent-editing risk.

## Use this when
Use this when reviewing scripts, docs, runbooks, dashboards, or generated outputs that require unstated assumptions.

## Failure smell
The workflow works only when someone remembers which machine, token, order, flag, or undocumented exception matters.

## Related doctrine
- [Systems Should Tell on Themselves](../../../docs/doctrines/systems-should-tell-on-themselves.md)
