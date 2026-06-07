---
id: antipattern:hidden-operational-context
title: Hidden Operational Context
type: antipattern
domain: operability
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  A system relies on unstated human knowledge to operate or diagnose safely.
concepts:
  - operability
  - context-regression
edges:
  contradicts:
    - note:context:hidden-context-is-operational-risk
origin:
  author: human
  review: manual
---

# Hidden Operational Context

## Failure mode
A system relies on unstated human knowledge to operate, diagnose, or recover safely.

## Detection
Reviewers cannot determine valid inputs, state, risks, or next actions from the source and generated evidence.
