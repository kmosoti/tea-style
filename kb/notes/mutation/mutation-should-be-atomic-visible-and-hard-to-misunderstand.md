---
id: note:mutation:mutation-should-be-atomic-visible-and-hard-to-misunderstand
title: Mutation Should Be Atomic Visible and Hard to Misunderstand
type: note
domain: automation
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Mutation should be deliberate, visible, bounded, and backed by evidence.
concepts:
  - mutation
  - evidence
  - change-control
  - validation
edges:
  supports:
    - note:evidence:systems-should-tell-on-themselves
    - doctrine:repo:engineering-control-spine
  contradicts:
    - antipattern:undocumented-mutation
origin:
  author: human
  review: manual
---

# Mutation Should Be Atomic Visible and Hard to Misunderstand

## Core claim
If a mutation happens, it should be atomic, visible, and hard to misunderstand.

## Why it matters
Invisible or ambiguous mutation is how automation creates incidents while appearing convenient.

## Use this when
Use this when reviewing automation, generated plans, CLIs, remediation scripts, or agent tools that can change state.

## Failure smell
A tool changes production state without a plan, dry-run, validation gate, change context, or structured result.

## Related doctrine
- [Safe Workflow Design](../../../domains/automation/safe-workflow-design.md)
- [Engineering Control Spine](../../../docs/doctrines/engineering-control-spine.md)
