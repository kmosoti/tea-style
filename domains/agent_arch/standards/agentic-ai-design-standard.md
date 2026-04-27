# Agentic AI Design Standard

## Purpose
Define how agentic AI systems should be designed, reviewed, and documented in this repository.

This standard is written for practical engineering work, especially VS Code GitHub Copilot Chat workflows.

## Core position

Agentic architecture is a control problem before it is a creativity problem.

The system should make it clear:

- what the agent is allowed to see
- what the agent is allowed to change
- what evidence proves completion
- when human review is required
- how durable knowledge is preserved

## Design order

Use this order before adding complexity:

1. Can deterministic code solve the task?
2. Can one model call solve the task?
3. Is retrieval needed?
4. Are tools needed?
5. Is a custom agent needed?
6. Are multiple agents actually justified?
7. Is memory needed?
8. Is the memory reviewed and compacted?

Do not start with multi-agent structure. Start with the smallest system that can be evaluated.

## Artifact hierarchy

| Layer | Role | Rule |
|---|---|---|
| Doctrine | Stable design stance | Keep in the knowledge base. |
| Repository instructions | Stable workspace behavior | Keep short and link outward. |
| Scoped instructions | Path-specific behavior | Use for repeated file or domain rules. |
| Custom agents | Role behavior | Keep narrow and tool-bounded. |
| Skills | Reusable procedures | Use for repeatable workflows. |
| TODO ledger | Current work plan | Keep reviewable. |
| Memory ledger | Durable lessons | Keep compact and curated. |

## Instructions first, agents second, memory third

### Instructions first
Instructions should define stable constraints:

- repository purpose
- tone
- forbidden behavior
- validation expectations
- documentation expectations

They should not try to encode every workflow.

### Agents second
Agents should represent real differences in responsibility:

- planner
- implementer
- tester
- auditor
- researcher

Do not create multiple agents when one scoped instruction would work.

### Memory third
Memory should be curated after repeated evidence. It should not be a raw transcript store.

A fact is memory-worthy when it changes future decisions.

## Context doctrine

Context is an input surface, not a dumping ground.

Good context is:

- relevant
- recent enough
- source-aware
- small enough to reason over
- explicit about uncertainty

Bad context is:

- a full transcript with no selection
- stale memory treated as fact
- unrelated file search results
- copied documentation without task relevance

## Tool doctrine

Tools should be exposed deliberately.

Prefer:

- read tools before write tools
- scoped write permissions
- explicit side-effect boundaries
- visible command output
- reversible changes where practical

Avoid:

- giving every agent every tool
- hiding destructive actions behind vague prompts
- letting workers change evaluators without approval

## Verification doctrine

Generation and verification must be separated.

A completion claim should rest on one or more of:

- command output
- tests
- lint or static checks
- link and path validation
- changed file inspection
- reviewed evidence in PR body

Do not accept `looks good` as verification.

## Karpathy-derived gate discipline

From the Autoresearch pattern, import the gate loop but not the reckless autonomy.

Use:

1. Baseline first.
2. Bound the mutation surface.
3. Keep the evaluator stable.
4. Compare result to acceptance criteria.
5. Persist result evidence.
6. Keep or discard the change.

For VS Code Copilot, this means:

- the planner defines the target and acceptance criteria
- the worker edits only the declared scope
- the tester verifies behavior without weakening the test
- the auditor checks the final artifact and records durable memory

## Knowledge-base doctrine

From the LLM Wiki pattern, separate three types of artifacts:

1. Research notes: source links, extracted claims, open questions.
2. Doctrine pages: stable principles and design standards.
3. Templates: copyable implementation scaffolds.

Do not mix these into one giant page.

## Memory compaction rule

A useful memory entry should answer:

- What changed?
- Why was it decided?
- What evidence supports it?
- What should future agents avoid repeating?

Memory should eventually graduate into:

- repository instructions
- standards
- templates
- checklists

If it never graduates, it should be pruned.

## Review checklist

Before accepting an agentic workflow design, ask:

- Is an agent actually needed?
- Is the role boundary real?
- Is tool access minimal?
- Is context intentionally selected?
- Is there a stable evaluator?
- Are side effects controlled?
- Is the handoff format explicit?
- Is memory curated?
- Can failures be diagnosed?
- Can a human resume the work from artifacts alone?

## Anti-patterns

Reject:

- one giant universal prompt
- many vague agents with overlapping authority
- workers that rewrite the plan while implementing
- agents that can weaken their own tests
- memory as transcript dumping
- planning without acceptance criteria
- summarization without audit
- broad workspace search before reading known target files
- speculative tool use when deterministic commands exist

## Standard phrase

No claim without artifact. No completion without verification. No memory without compaction.
