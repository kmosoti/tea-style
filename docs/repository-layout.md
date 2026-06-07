# Repository Layout

`tea-style` is a doctrine graph and preferences repository.

It exists to document how I prefer to design, structure, and review work across multiple technical domains, and to make that knowledge base inspectable through bounded lifecycle tooling.

## Domain layout

- `domains/coding/`
  - General software design, Python style, typing, abstractions, tests, and code review standards.
- `domains/agent_arch/`
  - Agent architecture, orchestration, context management, tool boundary preferences, and model doctrine.
  - `domains/agent_arch/models/` holds model taxonomy and inference mechanics references.
  - `domains/agent_arch/projects/` holds bounded learning/lab definitions.
- `domains/automation/`
  - Automation, configuration management, infrastructure, platform engineering, and workflow design.
- `domains/observability/`
  - Observability systems, telemetry pipelines, diagnostics, capacity thinking, and operational design.

## Repository-level docs

- `docs/repo-scope.md`
  - Purpose, audience, and scope boundaries.
- `docs/work-operating-model.md`
  - How issues/PRs are prepared, executed, and reviewed.
- `docs/page-template-standard.md`
  - Canonical structure for doctrine pages.
- `docs/second-brain-markdown-standard.md`
  - GitHub-native structure for maps of content, atomic pages, knowledge hooks, and related links.
- `docs/examples-and-diagrams-standard.md`
  - Rules for useful examples and diagrams.
- `docs/decisions/`
  - Decision log for durable architecture/doctrine decisions.
- `docs/maps/`
  - Human navigation maps for the doctrine graph.
- `docs/standards/`
  - Repository-wide graph, generated artifact, visualization, agent editing, and Python type standards.

## Cross cutting doctrine

- `docs/doctrines/`
  - Cross domain doctrine such as TEA Style and the engineering control spine.

## Knowledge base graph

- `kb/notes/`
  - Primary authored graph notes.
- `kb/concepts/`
  - Controlled vocabulary entries.
- `kb/antipatterns/`
  - Named failure modes.
- `kb/examples/`
  - Compact examples connected to doctrine.
- `graph/schema.md`
  - Graph schema reference.
- `graph/generated/`
  - Derived nodes, edges, chunks, reports, and visualizations.

## Lifecycle tooling

- `src/tea_kb/`
  - Python package for validation, graph construction, reporting, visualization, and export.
- `tests/`
  - Unit and integration tests for the lifecycle tool.
- `pyproject.toml`
  - Project metadata, dependencies, scripts, and tool configuration.

## Standard for domain content

Each domain should eventually capture:

1. Principles
2. Preferred patterns
3. Anti patterns
4. Tooling preferences
5. Examples

The goal is not encyclopedic documentation or product code. The goal is a clear record of how I prefer to build and reason, plus enough tooling to keep that record durable.
