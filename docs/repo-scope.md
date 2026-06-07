# Repository Scope

## Purpose
Define the explicit boundaries of `tea-style` so issues and PRs remain compact, reusable, and high signal.

## Core claim
`tea-style` is a Markdown-native doctrine graph with embedded lifecycle tooling. It is not a product codebase, a framework, a hosted app, or a general knowledge wiki.

## Definitions
- **Doctrine**: stable guidance for decisions, patterns, and tradeoffs.
- **Reference**: concise explanations, taxonomies, and standards used during implementation and review.
- **Doctrine graph**: authored Markdown knowledge units connected by explicit semantic edges.
- **Lifecycle tooling**: bounded Python support code that validates, builds, reports, visualizes, and exports the doctrine graph.
- **Agent legibility**: structure and wording that an LLM can parse and apply reliably.

## Positive scope
This repository includes:
- repository-level standards and operating model pages in `docs/`
- domain doctrine in `domains/<domain>/`
- patterns, anti-patterns, taxonomies, and decision records
- compact examples and diagrams when they improve understanding
- project/lab definitions for bounded learning exercises
- a Markdown-native knowledge base under `kb/`
- generated graph artifacts under `graph/generated/`
- bounded Python lifecycle tooling under `src/tea_kb/`

## Negative scope
This repository excludes:
- production applications and runtime systems
- framework scaffolding and boilerplate projects
- hosted services, SaaS, production APIs, and permanent background processes
- full RAG runtimes, model-calling systems, or chat interfaces
- graph database projects, RDF/OWL ontology projects, and Neo4j-first designs
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
`tea-style` is a doctrine/reference repository with compact examples and bounded lifecycle tooling. Markdown and frontmatter are canonical; generated artifacts and Python outputs are derived.

## Related pages
- [README.md](../README.md)
- [docs/repository-layout.md](repository-layout.md)
- [docs/work-operating-model.md](work-operating-model.md)
- [docs/standards/graph-knowledge-base-standard.md](standards/graph-knowledge-base-standard.md)
