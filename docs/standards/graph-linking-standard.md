---
id: standard:repo:graph-linking-standard
title: Graph Linking Standard
type: standard
domain: repo-wide
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Defines when to create semantic graph edges and when to rely on Markdown links.
concepts:
  - edges
  - linking
  - related links
  - graph hygiene
edges:
  supports:
    - standard:repo:graph-knowledge-base-standard
origin:
  author: human
  review: manual
---

# Graph Linking Standard

## Purpose
Control graph edge quality so the doctrine graph remains useful instead of becoming a link hairball.

## Core claim
Markdown links are for human navigation. Frontmatter edges are for semantic graph relationships.

## Definitions
- **Semantic edge**: a typed relationship that changes how the graph should be interpreted.
- **Loose relation**: a weak association that may not deserve an edge.
- **Link explosion**: too many low-value edges on a node.

## Rules / standards
- Create an edge only when the relationship is meaningful and reviewable.
- Prefer `supports`, `refines`, `depends_on`, `contradicts`, `applies_to`, `exemplifies`, or `supersedes` over `related_to`.
- Use `related_to` sparingly.
- `depends_on` and `supersedes` should be acyclic.
- Do not infer edges from shared words alone.
- Mark agent-inferred edges as proposed until reviewed.
- Every edge target must resolve to an authored node.

## Edge semantics
- `supports`: source strengthens target.
- `refines`: source makes target more specific.
- `depends_on`: source requires target to make sense.
- `contradicts`: source explicitly rejects target.
- `applies_to`: source is relevant to target.
- `exemplifies`: source demonstrates target.
- `supersedes`: source replaces target.
- `related_to`: source is loosely connected to target.

## Anti-patterns
- creating edges because two pages share a keyword
- overusing `related_to`
- using frontmatter edges for ordinary navigation
- creating edges to missing or planned nodes

## Related pages
- [graph-knowledge-base-standard.md](graph-knowledge-base-standard.md)
- [agent-kb-editing-standard.md](agent-kb-editing-standard.md)
