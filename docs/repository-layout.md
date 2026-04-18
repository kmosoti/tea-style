# Repository Layout

`tea-style` is a doctrine and preferences repository.

It exists to document how I prefer to design, structure, and review work across multiple technical domains.

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
- `docs/examples-and-diagrams-standard.md`
  - Rules for useful examples and diagrams.
- `docs/decisions/`
  - Decision log for durable architecture/doctrine decisions.

## Cross cutting doctrine

- `docs/doctrines/`
  - Cross domain doctrine such as TEA Style.

## Standard for domain content

Each domain should eventually capture:

1. Principles
2. Preferred patterns
3. Anti patterns
4. Tooling preferences
5. Examples

The goal is not encyclopedic documentation. The goal is a clear record of how I prefer to build and reason in each domain.
