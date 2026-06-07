---
id: standard:repo:agent-kb-editing-standard
title: Agent KB Editing Standard
type: standard
domain: agent-architecture
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Defines how agents may add or change graph knowledge without silently redefining doctrine.
concepts:
  - agent editing
  - review
  - provenance
  - proposed edges
edges:
  supports:
    - doctrine:repo:tea-style-doctrine
    - standard:repo:graph-linking-standard
  related_to:
    - doctrine:repo:systems-should-tell-on-themselves
origin:
  author: human
  review: manual
---

# Agent KB Editing Standard

## Purpose
Define how autonomous or assisted editing should change the doctrine graph safely.

## Core claim
Agents may propose graph changes. They must not silently promote inferred doctrine to reviewed doctrine.

## Rules / standards
- Prefer small notes over bloated pages.
- Reuse existing concepts before inventing new ones.
- Create concept notes when a concept becomes important.
- Do not create edges just because words are similar.
- Mark inferred edges as proposed unless the user explicitly reviewed them.
- Do not silently redefine core doctrine.
- Do not rename IDs casually.
- Update the `updated` frontmatter date when durable meaning, graph metadata, or relationships change.
- Run validation before finishing.
- Update maps only when navigation materially improves.

## Frontmatter policy
Agent-created note:

```yaml
origin:
  author: agent
  review: proposed
```

Human-reviewed agent note:

```yaml
origin:
  author: agent
  review: reviewed
```

Manual note:

```yaml
origin:
  author: human
  review: manual
```

## Agent PR checklist
- New notes are small and focused.
- IDs are stable and meaningful.
- Concepts reuse existing vocabulary.
- Edges are justified.
- `created` and `updated` dates are present and accurate enough for timeline generation.
- Generated artifacts are updated.
- Validation passes.
- Reports were reviewed.
- No unrelated restructuring was introduced.

## Related pages
- [graph-linking-standard.md](graph-linking-standard.md)
- [domains/agent_arch/control/deterministic-tool-boundaries.md](../../domains/agent_arch/control/deterministic-tool-boundaries.md)
