---
id: example:agents:agent-tool-boundary
title: Agent Tool Boundary
type: example
domain: agent-architecture
status: active
summary: >
  Agent tools should expose deterministic read, validation, dry-run, and mutation boundaries.
concepts:
  - agents
  - boundary
  - validation
edges:
  exemplifies:
    - note:boundaries:tools-should-make-boundaries-obvious
    - standard:repo:agent-kb-editing-standard
origin:
  author: human
  review: manual
---

# Agent Tool Boundary

## Example
```text
read_graph()
validate_plan(plan)
render_dry_run(plan)
execute_approved_plan(plan)
```

## Point
The agent proposes. Deterministic tools validate and execute within explicit boundaries.
