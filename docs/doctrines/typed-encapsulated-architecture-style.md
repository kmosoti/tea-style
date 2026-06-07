---
id: doctrine:repo:typed-encapsulated-architecture-style
title: Typed Encapsulated Architecture Style
type: doctrine
domain: repo-wide
status: active
created: 2026-03-27
updated: 2026-06-06
summary: >
  TEA is a decision style for explicit, modular, typed, reviewable, and durable systems.
concepts:
  - typing
  - encapsulation
  - architecture
  - contracts
  - operability
edges:
  supports:
    - doctrine:repo:tea-style-doctrine
  related_to:
    - doctrine:repo:engineering-control-spine
origin:
  author: human
  review: manual
---

# Typed Encapsulated Architecture Style

## Purpose
Define the core TEA doctrine for designing systems that are explicit, modular, reviewable, and durable.

## Core claim
Typed Encapsulated Architecture Style is a doctrine for building systems that are explicit, modular, reviewable, and durable.

## Knowledge hooks
- **Type**: cross-domain doctrine
- **Domain**: repository-wide
- **Concepts**: typing, encapsulation, architecture, contracts, operability
- **Use when**: evaluating whether a design fits the repository's core engineering taste

## Definitions
- **Typed**: important data, commands, config, results, and states have explicit structure.
- **Encapsulated**: internals are hidden behind narrow interfaces that make misuse harder.
- **Architecture**: dependencies, boundaries, state, and side effects are arranged deliberately.
- **Style**: a preference system for decisions, not a framework or runtime.

## Core ideas
- Prefer strong typing where it clarifies behavior.
- Keep modules black-boxed with narrow public interfaces.
- Separate configuration from execution.
- Prefer maintainable object-oriented structure where it improves consistency.
- Use protocols, factories, and interface-driven design when they reduce drift across implementations.
- Keep state and side effects explicit.
- Model contracts, errors, and results as first-class design concerns.
- Prefer feedback loops over one-way command assumptions.
- Keep dependencies lean.
- Prefer understandable code over clever code.

## Architecture / Mechanics
TEA is not a framework. It is a decision style.

It pushes work toward:
- validated inputs
- constrained side effects
- explicit contracts
- explicit state
- observable execution
- modular extension paths
- predictable review

The standard structure is:

```text
untrusted input
  -> validation and normalization
  -> typed domain objects
  -> pure planning or decision logic
  -> explicit side-effect boundary
  -> result, evidence, and feedback
```

## What TEA rejects
- architecture by novelty
- hidden global behavior
- configuration embedded deep inside logic
- abstractions without a real pressure behind them
- dependency growth without clear value
- state that readers must infer from call order
- mutation that cannot be dry-run, audited, or explained

## Standard question
When evaluating a design, the basic question is:

Does this make the system easier to understand, safer to extend, and easier to review?

If not, the complexity likely does not belong.

## Related pages
- [docs/doctrines/README.md](README.md)
- [engineering-control-spine.md](engineering-control-spine.md)
- [docs/second-brain-markdown-standard.md](../second-brain-markdown-standard.md)
