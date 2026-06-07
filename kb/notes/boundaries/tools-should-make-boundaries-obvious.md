---
id: note:boundaries:tools-should-make-boundaries-obvious
title: Tools Should Make Boundaries Obvious
type: note
domain: coding
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Tools should make read, write, validation, and execution boundaries visible.
concepts:
  - boundary
  - contract
  - mutation
  - validation
edges:
  supports:
    - doctrine:repo:engineering-control-spine
    - standard:repo:agent-kb-editing-standard
  applies_to:
    - map:coding:overview
    - map:agent-architecture:overview
origin:
  author: human
  review: manual
---

# Tools Should Make Boundaries Obvious

## Core claim
A tool should make its boundaries obvious: what it reads, what it writes, what it validates, and what it refuses to do.

## Why it matters
Ambiguous boundaries force humans and agents to infer safety from naming or prose. That is not enough for risky systems.

## Use this when
Use this when designing CLIs, automation clients, validators, exporters, or agent tools.

## Failure smell
A command sounds like a read but performs mutation, or a validator quietly fixes source files.

## Related doctrine
- [Architecture Boundaries](../../../domains/coding/architecture-boundaries.md)
- [Deterministic Tool Boundaries](../../../domains/agent_arch/control/deterministic-tool-boundaries.md)
