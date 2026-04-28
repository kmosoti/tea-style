# VS Code Copilot Handoff Hierarchy

## Purpose
Define a practical handoff workflow for using GitHub Copilot Chat in Visual Studio Code without relying on vague autonomous-agent behavior.

This workflow is designed for controlled engineering work where the user wants speed, auditability, and low drift.

## Core model

Use a gated hierarchy:

```text
Human
  -> Executive Planner
  -> Executive Worker
  -> Executive Tester
  -> Executive Auditor
  -> Memory and next-session handoff
```

The hierarchy is not a fantasy org chart. It is a set of boundaries.

Each tier answers a different question:

| Tier | Question | Output |
|---|---|---|
| Human | What outcome matters? | Goal and constraints |
| Planner | What should happen, in what order? | TODO ledger and handoff packages |
| Worker | What changed? | Bounded edit package |
| Tester | Does it work or satisfy evidence rules? | Verification result |
| Auditor | Is the work complete and durable? | Audit summary and memory update |

## Default workflow

### 1. Intake
The planner reads the request and identifies:

- goal
- scope
- out-of-scope items
- target files
- acceptance criteria
- validation method
- likely risks

### 2. Planning
The planner creates a small TODO ledger.

Each item should include:

- task
- target files
- acceptance criteria
- validation method
- owner role

### 3. Implementation
The worker receives one bounded task at a time.

The worker may:

- inspect relevant files
- make scoped edits
- update local docs when directly required

The worker may not:

- expand scope
- change acceptance criteria
- weaken tests
- rewrite unrelated files
- record durable memory without audit

### 4. Testing or validation
The tester verifies the changed artifact.

For code:

- run the relevant test command
- run lint or static checks if configured
- add or repair tests when behavior changed

For documentation:

- validate links and paths where practical
- check navigation updates
- check terminology consistency
- check that examples are copyable

### 5. Audit
The auditor checks:

- Does the diff match the task?
- Were the declared files changed?
- Were unrelated files changed?
- Is evidence present?
- Are risks documented?
- Should memory be updated?

### 6. Memory
Memory is updated only when the result is durable.

Examples of durable memory:

- a new workflow convention
- a stable repo structure decision
- a repeatedly useful command
- a known failure mode
- a decision that future agents must preserve

Examples of non-memory:

- temporary debug notes
- raw command output
- chat transcript fragments
- obvious facts already captured in docs

## Handoff package format

Use this structure when moving work between roles:

```md
## Task
<one bounded task>

## Context
<minimum needed context>

## Target files
- `<path>`

## Allowed changes
- <what may be edited>

## Forbidden changes
- <what must not be touched>

## Acceptance criteria
- <observable done condition>

## Validation
- <commands or inspection steps>

## Return format
- files changed
- summary
- validation evidence
- unresolved issues
```

## Fan-out rule

Fan-out only when tasks are independent.

Good fan-out:

- Worker A edits source behavior.
- Worker B writes tests against the declared behavior.
- Worker C checks documentation gaps.

Bad fan-out:

- three workers all improve the architecture
- multiple agents editing the same file without a merge strategy
- a tester changing the acceptance criteria
- a summarizer making implementation changes

## VS Code Copilot artifact layout

When implementing this workflow inside VS Code, prefer this eventual layout:

```text
.github/
  copilot-instructions.md
  instructions/
    agentic-workflow.instructions.md
    python-quality.instructions.md
    docs-sync.instructions.md
  agents/
    executive-planner.agent.md
    executive-worker.agent.md
    executive-tester.agent.md
    executive-auditor.agent.md
  skills/
    repo-memory/
      SKILL.md
    knowledge-lint/
      SKILL.md
```

This repository currently keeps the doctrine under `domains/agent_arch/`. Active `.github` implementation files should be added only when the repo intentionally becomes a live Copilot customization testbed.

## Planning checklist

Before worker handoff, planner must answer:

- What is the smallest useful unit of work?
- What files are likely involved?
- What files are explicitly out of scope?
- What command or inspection proves completion?
- What failure mode is most likely?
- Does this require memory after completion?

## Worker checklist

Before returning control, worker must answer:

- What changed?
- Why was it needed?
- What files were touched?
- What was not touched?
- What evidence exists?
- What risk remains?

## Tester checklist

Tester must answer:

- What behavior or artifact was validated?
- What command or inspection was used?
- What failed first, if anything?
- Was the evaluator changed?
- Are there coverage gaps?

## Auditor checklist

Auditor must answer:

- Did the work match the plan?
- Did the evidence match the claim?
- Did any scope creep occur?
- Does navigation need updating?
- Should memory be updated?
- Can a future session resume from the artifacts?

## Failure handling

If work fails verification:

1. Do not summarize as complete.
2. Mark the failed item unresolved.
3. Preserve the command or inspection result.
4. Route back to the worker with a narrow fix task.
5. Re-run validation.

If the failure is outside scope:

1. Document it as a discovered issue.
2. Do not absorb it into the current work without approval.
3. Create a follow-up item.

## Drift controls

Use these controls to reduce agent drift:

- keep the task ledger visible
- use narrow handoff packages
- avoid broad workspace search unless needed
- prefer known target files over speculative discovery
- require evidence for completion claims
- keep memory curated
- separate planning, editing, validation, and audit

## Best-use cases

Use this workflow for:

- repo restructuring
- doctrine expansion
- documentation systems
- Python feature work
- test repair
- multi-file refactors
- agent instruction design

Do not use this workflow for:

- tiny one-line edits
- exploratory reading with no deliverable
- cases where a deterministic script is better
- sensitive or destructive actions without human approval
