---
id: concept:boundary
title: Boundary
type: concept
domain: coding
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  A public interface where messy internals, external systems, or side effects are contained.
concepts:
  - boundary
  - encapsulation
edges:
  related_to:
    - doctrine:repo:engineering-control-spine
origin:
  author: human
  review: manual
---

# Boundary

## Definition
A boundary is a public interface where messy internals, external systems, or side effects are contained.

## Use
Use boundaries to keep callers dependent on behavior instead of implementation details.
