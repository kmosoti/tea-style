---
id: decision:repo:0002-adopt-markdown-native-doctrine-graph
title: Adopt Markdown-Native Doctrine Graph
type: decision
domain: repo-wide
status: active
summary: >
  Markdown notes and frontmatter are the source of truth; graph artifacts are generated from visible source files.
concepts:
  - markdown
  - frontmatter
  - graph
  - generated artifacts
edges:
  supports:
    - doctrine:repo:tea-style-doctrine
    - standard:repo:graph-knowledge-base-standard
  refines:
    - decision:repo:0001-adopt-github-native-second-brain-doctrine
origin:
  author: human
  review: manual
---

# 0002-adopt-markdown-native-doctrine-graph

## Status
accepted

## Context
`tea-style` needs second-brain behavior that is inspectable in GitHub, useful to humans, and consumable by future autonomous systems.

## Decision
Use Markdown notes and YAML frontmatter as the canonical source of the doctrine graph.

Generated artifacts such as JSONL files, reports, chunks, and visualizations are derived from source Markdown. They are useful for review and consumption, but they are not canonical.

## Rationale
Markdown keeps authorship visible. Frontmatter gives the graph enough structure to validate and export. This avoids pushing the repository into a database-first or product-runtime shape.

## Consequences
- Authored graph nodes must use stable IDs.
- Generated artifacts can be rebuilt from source.
- Markdown links remain for human navigation.
- Frontmatter edges carry semantic graph relationships.

## Related pages/decisions
- [docs/standards/graph-knowledge-base-standard.md](../standards/graph-knowledge-base-standard.md)
- [docs/standards/generated-artifact-standard.md](../standards/generated-artifact-standard.md)
- [docs/doctrines/tea-style-doctrine.md](../doctrines/tea-style-doctrine.md)
