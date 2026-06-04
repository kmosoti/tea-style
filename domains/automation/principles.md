# Automation Principles

## Core preferences
- prefer idempotent behavior
- keep source of truth explicit
- separate control plane concerns from execution plane concerns
- favor diagnosable workflows over opaque cleverness
- reduce drift through structure, not heroics
- plan before mutating
- encode validation gates and blast-radius limits
- model workflow state explicitly
- collect evidence at every risky step
- reconcile desired state with actual state

## Related pages
- [safe-workflow-design.md](safe-workflow-design.md)
- [change-management.md](change-management.md)
- [configuration-management.md](configuration-management.md)
- [docs/doctrines/engineering-control-spine.md](../../docs/doctrines/engineering-control-spine.md)
