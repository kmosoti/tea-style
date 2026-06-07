---
id: standard:repo:python-type-discipline
title: Python Type Discipline
type: standard
domain: coding
status: active
created: 2026-06-06
updated: 2026-06-06
summary: >
  Defines how tea_kb uses Pydantic, dataclasses, NewType, StrEnum, Protocol, and standard collections.
concepts:
  - typing
  - pydantic
  - dataclasses
  - protocols
  - static analysis
edges:
  supports:
    - doctrine:repo:typed-encapsulated-architecture-style
  applies_to:
    - standard:repo:generated-artifact-standard
origin:
  author: human
  review: manual
---

# Python Type Discipline

## Purpose
Define the type discipline for the `tea_kb` lifecycle tool.

## Core claim
Use the lowest type layer that solves the problem.

## Definitions
- **Boundary model**: Pydantic model used to validate untrusted Markdown/frontmatter/config input.
- **Domain model**: frozen dataclass used inside trusted core logic.
- **Semantic ID**: `NewType` wrapper for IDs that should not be casually mixed.
- **Protocol**: small behavior contract used at module boundaries.

## Rules / standards
- Use Pydantic at file/config boundaries.
- Use frozen slots dataclasses for internal graph objects.
- Use `NewType` for node, edge, chunk, and concept IDs.
- Use `StrEnum` for node and edge categories.
- Use `Protocol` for reader, exporter, and validator behavior.
- Use `collections.abc` for function input typing.
- Use `defaultdict`, `Counter`, and `deque` for graph support where appropriate.
- Keep domain code independent of Typer, Rich, PyVis, and filesystem details.

## Tool mapping
| Problem | Tool |
|---|---|
| Frontmatter validation | Pydantic |
| Config validation | Pydantic |
| Internal graph objects | frozen slots dataclasses |
| Semantic IDs | `NewType` |
| Node/edge categories | `StrEnum` |
| Plugin-like behavior | `Protocol` |
| Function input typing | `collections.abc` |
| Concept frequency | `Counter` |
| Graph traversal | `deque` |

## Related pages
- [domains/coding/architecture-boundaries.md](../../domains/coding/architecture-boundaries.md)
- [docs/doctrines/typed-encapsulated-architecture-style.md](../doctrines/typed-encapsulated-architecture-style.md)
