---
id: standard:repo:graph-knowledge-base-standard
title: Graph Knowledge Base Standard
type: standard
domain: repo-wide
status: active
created: 2026-06-06
updated: 2026-06-07
summary: >
  Defines graph source units, node types, edge types, IDs, frontmatter, and generated artifacts.
concepts:
  - graph
  - frontmatter
  - node
  - edge
  - generated artifacts
edges:
  supports:
    - doctrine:repo:tea-style-doctrine
  depends_on:
    - decision:repo:0002-adopt-markdown-native-doctrine-graph
origin:
  author: human
  review: manual
---

# Graph Knowledge Base Standard

## Purpose
Define the canonical Markdown graph model for `tea-style`.

## Core claim
Markdown notes and frontmatter are the authored source of truth. Graph artifacts are generated from that source.

## Definitions
- **Note**: primary authored graph node.
- **Chunk**: generated search unit derived from a node section.
- **Concept**: controlled vocabulary entry.
- **Frontmatter edge**: semantic relationship between graph nodes.
- **Generated artifact**: derived JSONL, report, or visualization.

## Rules / standards
- Use industry terms in schema, code, exports, and validators.
- Use tea-themed language only in prose, aliases, section flavor, and report titles.
- Use readable IDs instead of UUIDs.
- Keep authored notes smaller than broad doctrine pages.
- Do not make every Markdown link a graph edge.
- Do not make every Markdown section a graph node.
- Do not treat generated artifacts as canonical.

## Node types
Use only:
- `note`
- `doctrine`
- `concept`
- `antipattern`
- `decision`
- `example`
- `standard`
- `map`

## Edge types
Use only:
- `supports`
- `refines`
- `depends_on`
- `contradicts`
- `applies_to`
- `exemplifies`
- `supersedes`
- `related_to`

## ID rules
IDs are lowercase, kebab-case, type-prefixed, and stable after creation.

Preferred form:

```text
<type>:<domain-or-category>:<slug>
```

Concept and antipattern IDs may use:

```text
concept:<slug>
antipattern:<slug>
```

## Required frontmatter
```yaml
id: note:evidence:example
title: Example
type: note
domain: repo-wide
status: active
created: 2026-06-07
updated: 2026-06-07
concepts:
  - evidence
```

## Timeline metadata
Every authored graph node should carry:
- `created`: the date the note, concept, decision, standard, map, example, or antipattern entered the graph.
- `updated`: the latest meaningful doctrine or metadata update date.

Use ISO `YYYY-MM-DD` dates. Generated timeline artifacts use these fields rather than Git history so timelines remain portable across forks, exports, and future search systems.

When backfilling existing notes, prefer Git first-seen date for `created` and latest meaningful source change date for `updated`. When editing a note later, keep `created` stable and move `updated` to the edit date.

## Related pages
- [graph/schema.md](../../graph/schema.md)
- [graph-linking-standard.md](graph-linking-standard.md)
- [generated-artifact-standard.md](generated-artifact-standard.md)
