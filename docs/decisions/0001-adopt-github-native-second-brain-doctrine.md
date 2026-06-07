---
id: decision:repo:0001-adopt-github-native-second-brain-doctrine
title: Adopt GitHub-Native Second-Brain Doctrine
type: decision
domain: repo-wide
status: active
created: 2026-06-04
updated: 2026-06-06
summary: >
  Use GitHub-native Markdown as the second-brain substrate for tea-style.
concepts:
  - second brain
  - markdown
  - maps of content
  - related links
edges:
  supports:
    - standard:repo:graph-knowledge-base-standard
  related_to:
    - doctrine:repo:tea-style-doctrine
origin:
  author: human
  review: manual
---

# 0001-adopt-github-native-second-brain-doctrine

## Status
accepted

## Context
`tea-style` is a doctrine/reference repository for humans and agents. It needs second-brain retrieval behavior without depending on non-GitHub tools or private note-system syntax.

## Decision
Use GitHub-native Markdown as the second-brain substrate.

Pages should use:
- atomic concepts
- map-of-content README/index pages
- compact knowledge hooks
- relative Markdown links
- related pages sections
- decision records for durable why

## Rationale
This keeps the repository readable in GitHub, easy to clone, easy for agents to parse, and independent of local note-taking applications.

## Consequences
- New substantial doctrine pages should include knowledge hooks.
- README and index pages should act as maps of content.
- Wiki-link syntax and plugin-specific metadata should be avoided.
- Cross-domain concepts should be linked rather than duplicated.

## Related pages/decisions
- [docs/second-brain-markdown-standard.md](../second-brain-markdown-standard.md)
- [docs/page-template-standard.md](../page-template-standard.md)
- [docs/doctrines/engineering-control-spine.md](../doctrines/engineering-control-spine.md)
