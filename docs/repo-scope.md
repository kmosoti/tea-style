# Repository Scope

## Purpose
Define the explicit boundaries of `tea-style` so issues and PRs remain compact, reusable, and high signal.

## Core claim
`tea-style` is a doctrine and reference repository. It is not a product codebase, a framework, or a general knowledge wiki.

## Definitions
- **Doctrine**: stable guidance for decisions, patterns, and tradeoffs.
- **Reference**: concise explanations, taxonomies, and standards used during implementation and review.
- **Agent legibility**: structure and wording that an LLM can parse and apply reliably.

## Positive scope
This repository includes:
- repository-level standards and operating model pages in `docs/`
- domain doctrine in `domains/<domain>/`
- patterns, anti-patterns, taxonomies, and decision records
- compact examples and diagrams when they improve understanding
- project/lab definitions for bounded learning exercises

## Negative scope
This repository excludes:
- production applications and runtime systems
- framework scaffolding and boilerplate projects
- vendor news summaries and trend commentary
- long unstructured notes dumps
- decorative examples and decorative diagrams

## Audience
Primary readers are:
- engineers who want explicit architecture and review standards
- LLM-based assistants that need predictable structure and precise definitions

## Human readability and agent legibility
Pages should be:
- short enough to scan quickly
- explicit enough to execute without guessing
- structured with stable headings and definitions
- internally linked so navigation is mechanical

## Repository identity
`tea-style` is a doctrine/reference repository with compact examples. It is not a product repo and not a broad wiki.

## Related pages
- `README.md`
- `docs/repository-layout.md`
- `docs/work-operating-model.md`
