---
id: concept:mutation
title: Mutation
type: concept
domain: automation
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  An operation that changes system, repository, workflow, or external state.
concepts:
  - mutation
edges:
  related_to:
    - note:mutation:mutation-should-be-atomic-visible-and-hard-to-misunderstand
origin:
  author: human
  review: manual
---

# Mutation

## Definition
Mutation is an operation that changes system, repository, workflow, or external state.

## Use
Use this concept when separating reads from writes and planning validation gates.
