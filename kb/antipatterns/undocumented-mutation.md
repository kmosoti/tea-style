---
id: antipattern:undocumented-mutation
title: Undocumented Mutation
type: antipattern
domain: automation
status: active
summary: >
  A tool mutates state without clear plan, boundary, evidence, or recovery path.
concepts:
  - mutation
  - evidence
edges:
  contradicts:
    - note:mutation:mutation-should-be-atomic-visible-and-hard-to-misunderstand
origin:
  author: human
  review: manual
---

# Undocumented Mutation

## Failure mode
A tool mutates state without making the mutation visible, reviewable, or recoverable.

## Detection
Mutation is hidden inside read-sounding commands, broad scripts, prose-only output, or implicit side effects.
