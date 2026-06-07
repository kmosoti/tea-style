---
id: note:test:valid-note
title: Valid Note
type: note
domain: test
status: active
summary: >
  A valid test note.
concepts:
  - evidence
edges:
  supports:
    - concept:evidence
origin:
  author: human
  review: manual
---

# Valid Note

## Core claim
This note is valid.

## Why it matters
It exercises frontmatter parsing.

## Use this when
Use this in tests.

## Failure smell
The parser rejects a valid file.
