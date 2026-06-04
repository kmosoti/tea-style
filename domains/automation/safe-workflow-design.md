# Safe Workflow Design

## Purpose
Define how TEA expects infrastructure and platform automation workflows to be planned, executed, observed, and recovered.

## Core claim
Serious automation is not just a script. It is a controlled workflow with state, policy, evidence, and feedback.

## Knowledge hooks
- **Type**: domain doctrine
- **Domain**: automation
- **Concepts**: idempotency, planning, state machines, validation gates, reconciliation, compensation, blast radius
- **Use when**: designing automation that reads or mutates infrastructure, configuration, clusters, services, or tickets

## Definitions
- **Plan**: a structured description of intended targets, steps, risks, gates, expected mutations, and evidence.
- **Execution**: the side-effecting phase that consumes an approved plan.
- **Validation gate**: a precondition or postcondition check around risky work.
- **State machine**: explicit workflow states and allowed transitions.
- **Idempotency**: repeated execution does not create unintended additional effects.
- **Compensation**: a recovery action when true rollback is not available.
- **Reconciliation**: compare desired state with actual state and converge safely.
- **Blast radius**: the maximum allowed impact of an action or failure.

## Architecture / Mechanics
Use this workflow shape:

```text
request
  -> context and policy validation
  -> plan
  -> dry-run or review
  -> gated execution
  -> checkpoint
  -> reconcile actual state
  -> evidence report
```

Mutating workflows should record enough state to answer:
- what ran
- who or what requested it
- what target was affected
- which step is current or terminal
- what changed
- what failed
- what evidence was collected
- whether resume is safe

## Patterns
- Generate a plan before mutation.
- Separate commands from queries.
- Use typed command, context, result, and report objects.
- Encode maintenance windows, change IDs, approvals, and environment rules as policy.
- Use state machines for workflows with retries, rollback, compensation, or resume.
- Make every step idempotent or document why it is not.
- Use deadlines and cancellation rules for long-running work.
- Parallelize reads aggressively and serialize risky writes deliberately.
- Use rate limits, circuit breakers, queues, and backpressure when dependencies can be overloaded.
- Use reconciliation loops for systems that may be eventually consistent.
- Capture structured logs, metrics, correlation IDs, and redacted evidence.

## Anti-patterns
- one function that loads config, gets secrets, calls APIs, mutates hosts, logs prose, and prints output
- API timeout treated as proof that mutation failed
- production change without a change ID or approval path
- dry-run that still calls mutation APIs
- hidden retry loops that can amplify incidents
- plan output that cannot be diffed or reviewed
- reports that are prose-only instead of structured evidence rendered as prose

## Example state model
```text
PENDING
PRECHECKING
PLANNED
APPROVED
EXECUTING
RECONCILING
COMPLETED
FAILED
COMPENSATING
BLOCKED
```

Allowed transitions should be explicit. For example, `COMPLETED -> EXECUTING` should not happen without a new request.

## Related pages
- [principles.md](principles.md)
- [change-management.md](change-management.md)
- [configuration-management.md](configuration-management.md)
- [examples/change-safe-automation-pattern.md](examples/change-safe-automation-pattern.md)
- [docs/doctrines/engineering-control-spine.md](../../docs/doctrines/engineering-control-spine.md)
- [domains/observability/principles.md](../observability/principles.md)
