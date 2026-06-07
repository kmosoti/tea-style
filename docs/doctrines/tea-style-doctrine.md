---
id: doctrine:repo:tea-style-doctrine
title: TEA Style Doctrine
type: doctrine
domain: repo-wide
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  tea-style is a Markdown-native engineering doctrine graph with embedded Python lifecycle tooling.
concepts:
  - doctrine graph
  - lifecycle tooling
  - markdown
  - context regression
edges:
  supports:
    - doctrine:repo:systems-should-tell-on-themselves
  depends_on:
    - decision:repo:0002-adopt-markdown-native-doctrine-graph
    - decision:repo:0003-ship-tea-kb-lifecycle-tooling
  related_to:
    - doctrine:repo:typed-encapsulated-architecture-style
origin:
  author: human
  review: manual
---

# TEA Style Doctrine

## Purpose
Define the repository's current identity as both doctrine graph and bounded lifecycle tool.

## Core claim
`tea-style` is a Markdown-native engineering doctrine graph with embedded Python lifecycle tooling.

## Definitions
- **Markdown-native**: authored Markdown and frontmatter are the source of truth.
- **Doctrine graph**: notes, concepts, decisions, standards, examples, and antipatterns connected by explicit semantic edges.
- **Lifecycle tooling**: local Python code that validates, builds, reports, visualizes, and exports the graph.
- **Context regression**: repeated rediscovery of knowledge that should have been captured as durable doctrine.

## Architecture / Mechanics
The repository has three layers:

```text
authored Markdown/frontmatter
  -> generated graph artifacts and reports
  -> future consumers such as agents, search, and review workflows
```

The Python tool supports the knowledge base. It does not define doctrine by itself.

## Patterns
- Capture durable learning as small graph notes.
- Use concepts to prevent vocabulary drift.
- Use frontmatter edges for semantic graph relationships.
- Use Markdown links for human navigation.
- Commit deterministic generated artifacts when they improve review.

## Anti-patterns
- treating generated artifacts as canonical
- turning the repository into a hosted product
- adding cute tea-themed names to schema or code
- letting agents create reviewed doctrine silently

## Related pages
- [systems-should-tell-on-themselves.md](systems-should-tell-on-themselves.md)
- [engineering-control-spine.md](engineering-control-spine.md)
- [docs/standards/graph-knowledge-base-standard.md](../standards/graph-knowledge-base-standard.md)
- [docs/standards/agent-kb-editing-standard.md](../standards/agent-kb-editing-standard.md)
