# Deterministic Tool Boundaries

## Purpose
Define how agent-assisted systems should use tools without letting generated text bypass engineering controls.

## Core claim
LLMs should propose, summarize, classify, and draft. Deterministic tools should validate, diff, test, enforce policy, and execute risky work.

## Knowledge hooks
- **Type**: domain doctrine
- **Domain**: agent architecture
- **Concepts**: tool boundaries, validators, dry-run, policy checks, human approval, evidence
- **Use when**: designing an agent workflow that can affect code, infrastructure, data, tickets, or external systems

## Definitions
- **Deterministic tool**: a checker or executor with predictable behavior for the same inputs.
- **Plan validator**: a tool that rejects malformed, unsafe, or policy-violating plans.
- **Tool boundary**: the interface between generated intent and verified action.
- **Human approval gate**: a review point for risky, ambiguous, destructive, or policy-sensitive actions.

## Architecture / Mechanics
Use this control path:

```text
LLM proposal
  -> schema validation
  -> policy validation
  -> diff or dry-run
  -> deterministic execution
  -> evidence capture
  -> human review when risk justifies it
```

The agent should not be the only judge of whether its own output is safe.

## Patterns
- Use schemas for commands, plans, configs, and messages.
- Use static analysis, tests, linters, contract tests, and dry-run executors as gates.
- Separate read tools from write tools.
- Expose only tools relevant to the current task.
- Require approval for destructive, irreversible, or high-blast-radius actions.
- Capture evidence in structured form so humans can review outcomes.
- Keep local examples and docs close to the code or doctrine they support.

## Anti-patterns
- agents executing free-form generated shell against production-like targets
- policy encoded only in prompt text
- broad tool access without task-specific need
- hidden write operations inside tools that sound read-only
- plan approval based only on fluent prose
- no record of what the agent changed, checked, or skipped

## Related pages
- [guardrails.md](guardrails.md)
- [human-in-the-loop.md](human-in-the-loop.md)
- [tool-exposure.md](tool-exposure.md)
- [docs/doctrines/engineering-control-spine.md](../../../docs/doctrines/engineering-control-spine.md)
- [domains/automation/safe-workflow-design.md](../../automation/safe-workflow-design.md)
