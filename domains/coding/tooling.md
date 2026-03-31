# Coding Tooling

## Baseline tools
- `black` for deterministic formatting
- `ruff` for linting and lightweight static checks
- `mypy` for type checking
- `venv` or equivalent lightweight virtual environments

## Tooling stance
Tooling should reduce drift and review friction. It should not become a dependency stack of its own.

## Dependency preference
Prefer the least necessary libraries. A small dependency surface is easier to audit, upgrade, and reason about.
