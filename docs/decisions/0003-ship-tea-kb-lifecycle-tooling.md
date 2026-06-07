---
id: decision:repo:0003-ship-tea-kb-lifecycle-tooling
title: Ship TEA KB Lifecycle Tooling
type: decision
domain: repo-wide
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Include a bounded Python package and CLI for validating, building, reporting, visualizing, and exporting the Markdown doctrine graph.
concepts:
  - lifecycle tooling
  - validation
  - graph
  - reports
  - visualization
edges:
  supports:
    - doctrine:repo:tea-style-doctrine
    - standard:repo:generated-artifact-standard
  depends_on:
    - decision:repo:0002-adopt-markdown-native-doctrine-graph
origin:
  author: human
  review: manual
---

# 0003-ship-tea-kb-lifecycle-tooling

## Status
accepted

## Context
The repository is becoming a doctrine graph. Manual review alone will not reliably catch duplicate IDs, invalid edges, stale generated artifacts, broken links, orphan notes, or concept drift.

## Decision
Add a Python package named `tea_kb` and a CLI named `tea-kb`.

The tool may:
- read Markdown
- parse frontmatter
- validate schema and graph consistency
- extract sections and chunks
- build graph artifacts
- generate reports
- generate diagnostic visualizations
- support agent-safe iteration

The tool must not become a hosted service, production API, full RAG runtime, chat interface, or permanent background process.

## Rationale
Bounded lifecycle tooling makes the knowledge base durable and inspectable while staying inside the repository's doctrine/reference scope.

## Consequences
- Python implementation code belongs under `src/tea_kb/`.
- Tests belong under `tests/`.
- Generated artifacts should be deterministic.
- CI should run validation and stale-artifact checks.

## Related pages/decisions
- [docs/standards/python-type-discipline.md](../standards/python-type-discipline.md)
- [docs/standards/generated-artifact-standard.md](../standards/generated-artifact-standard.md)
- [docs/repo-scope.md](../repo-scope.md)
