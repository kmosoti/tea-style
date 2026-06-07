---
id: doctrine:repo:engineering-control-spine
title: Engineering Control Spine
type: doctrine
domain: repo-wide
status: active
created: 2026-06-07
updated: 2026-06-07
summary: >
  Good systems are easy to reason about, easy to change, hard to misuse, and observable when they fail.
concepts:
  - change control
  - boundaries
  - state
  - contracts
  - feedback loops
  - operability
edges:
  refines:
    - doctrine:repo:typed-encapsulated-architecture-style
  supports:
    - doctrine:repo:systems-should-tell-on-themselves
  applies_to:
    - map:repo:engineering-doctrine
origin:
  author: human
  review: manual
---

# Engineering Control Spine

## Purpose
Define the cross-domain engineering model behind TEA beyond any single pattern such as AOP.

## Core claim
Good systems are easy to reason about, easy to change, hard to misuse, and observable when they fail.

## Knowledge hooks
- **Type**: cross-domain doctrine
- **Domain**: repository-wide
- **Concepts**: change control, boundaries, state, contracts, feedback loops, operability
- **Use when**: designing, reviewing, or refactoring systems that must survive real change and failure

## Definitions
- **Change control**: explicit handling of what can change, who approves it, how it is validated, and how it is recovered.
- **Boundary**: a public interface where messy internals, external systems, or side effects are contained.
- **State**: the modeled condition of a system, workflow, object, or external dependency.
- **Contract**: a promise about inputs, outputs, side effects, errors, compatibility, or behavior.
- **Feedback loop**: a sense-decide-act-verify cycle that compares desired state with actual state.
- **Operability**: the ability to run, diagnose, recover, audit, and safely evolve a system.

## Architecture / Mechanics
Use these six control surfaces when evaluating design:

1. **Boundaries**
   - Encapsulation, ports/adapters, dependency injection, protocols, anti-corruption layers.
   - Goal: callers depend on behavior, not implementation details.

2. **State**
   - Typed domain models, invariants, immutable plans, state machines, checkpoints, resume rules.
   - Goal: valid states are explicit and invalid states are difficult to construct.

3. **Contracts**
   - Command/query separation, result objects, error taxonomy, schema validation, versioning, backward compatibility.
   - Goal: readers know what a component promises and what can fail.

4. **Change control**
   - Planning before execution, dry-run, validation gates, progressive delivery, blast-radius limits, feature flags, kill switches, human approval.
   - Goal: mutation is deliberate, reviewable, and bounded.

5. **Feedback loops**
   - Idempotency, reconciliation, polling with deadlines, retries with discipline, circuit breakers, backpressure, rate limiting.
   - Goal: the system converges safely instead of assuming a command worked.

6. **Operability**
   - Structured logs, metrics, traces, correlation IDs, evidence, reports, runbooks, data lineage, reproducibility.
   - Goal: operators can answer what ran, why it ran, what changed, what failed, and what evidence proves it.

## Priority patterns
- typed domain models
- dependency injection and protocols
- functional core with imperative shell
- planning separate from execution
- state machines for long workflows
- validation gates before risky work
- idempotent commands and reconciliation loops
- explicit error/result/evidence models
- ports and adapters for external systems
- contract tests for external APIs
- observability-driven development

## Anti-patterns
- hidden mutation inside read-sounding functions
- global state that controls behavior implicitly
- raw dictionaries flowing through core logic
- giant procedural scripts that mix config, validation, transport, logging, and mutation
- retries without idempotency or reconciliation
- docs that describe safety without code enforcing it
- LLM-generated plans that bypass deterministic validation

## Review questions
Ask these before adding or changing a system:

1. What domain concept is being modeled?
2. What is the clean input and output?
3. What state can this be in?
4. What invariants must always hold?
5. What can fail?
6. Is this read-only or mutating?
7. Is it idempotent?
8. Can it dry-run?
9. Can it validate before and after?
10. What evidence proves it worked?
11. Can the logic be tested without touching real systems?
12. Can the external system be swapped later?
13. Will a teammate or agent understand the boundary?

## Related pages
- [typed-encapsulated-architecture-style.md](typed-encapsulated-architecture-style.md)
- [docs/second-brain-markdown-standard.md](../second-brain-markdown-standard.md)
- [domains/coding/architecture-boundaries.md](../../domains/coding/architecture-boundaries.md)
- [domains/automation/safe-workflow-design.md](../../domains/automation/safe-workflow-design.md)
- [domains/agent_arch/control/deterministic-tool-boundaries.md](../../domains/agent_arch/control/deterministic-tool-boundaries.md)
