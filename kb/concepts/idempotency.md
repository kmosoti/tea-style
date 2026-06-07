---
id: concept:idempotency
title: Idempotency
type: concept
domain: automation
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Repeating an operation does not cause unintended additional effects.
concepts:
  - idempotency
edges:
  related_to:
    - doctrine:repo:engineering-control-spine
origin:
  author: human
  review: manual
---

# Idempotency

## Definition
Idempotency means running an operation repeatedly does not cause unintended additional effects.

## Use
Use idempotency when designing retries, resume behavior, reconciliation, and automation safety.
