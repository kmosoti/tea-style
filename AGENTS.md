# AGENTS.md

## Repository identity

`tea-style` is a compact doctrine and reference repository for engineering architecture.
It is written for both human engineers and LLM-based assistants.

TEA stands for Typed Encapsulated Architecture Style.

This repository is:
- a doctrine repo
- a reference repo
- a standards/patterns repo
- a place for compact examples and architecture diagrams when they increase clarity

This repository is not:
- a product repo
- a framework repo
- a general tutorial dump
- a blog
- a random notes archive
- a place to add implementation code unless the issue explicitly calls for it

## Primary objective

Optimize for:
- compactness
- precision
- explicit definitions
- durable structure
- high signal-to-noise
- reusability
- consistency across pages
- usefulness to both engineers and agents

Prefer clear structure and crisp distinctions over broad coverage.

## Repository layout

Use these defaults:
- `README.md`: repository overview and identity
- `docs/`: repository-wide scope, standards, working model, and decision records
- `domains/`: peer doctrine domains such as coding, agent architecture, automation, and observability

Use these rules:
- put repository-wide governance and standards in `docs/`
- put domain-specific doctrine in `domains/<domain>/`
- add new folders only when there is a clear structural need
- do not create parallel structures that duplicate existing concepts

## Content that belongs here

Valid artifacts include:
- doctrine pages
- taxonomy pages
- architecture explanations
- patterns and anti-patterns
- standards and conventions
- decision records
- compact examples
- architecture diagrams
- project/lab definitions for learning or experimentation

Avoid adding:
- large runnable systems
- production app scaffolding
- generic sample projects
- vendor-news summaries
- long unstructured research dumps
- decorative diagrams
- filler examples

## Mandatory pre-edit workflow

Before editing any files:
1. inspect the repository structure
2. inspect the relevant issue(s)
3. identify the requested deliverable(s)
4. classify the issue into a work pipeline
5. detect dependencies, restructuring risk, and conflict risk
6. determine whether the issue is safe to execute in parallel with others
7. decide whether temporary helper tooling would materially improve speed or consistency
8. produce a short plan if the task is ambiguous, structural, or high-risk
9. only then implement changes

Do not jump directly into editing when the issue is under-specified or structurally risky.

## Work pipeline classification

Every issue should be classified before implementation.

### Pipeline A: Additive doctrine work
Use for:
- new markdown doctrine pages
- standards pages
- taxonomy pages
- primers
- README/index additions
- examples/diagram guidance
- scope and operating-model documents

Characteristics:
- low structural risk
- usually parallel-safe
- minimal repo conflict potential

### Pipeline B: Structural or refactoring work
Use for:
- moving directories
- renaming or reorganizing sections
- changing navigation structure
- redefining repository layout
- changing canonical locations of existing concepts
- any work likely to conflict with several other issues

Characteristics:
- high conflict risk
- planning required before implementation
- should not be executed casually in parallel with adjacent structural work

### Pipeline C: Support tooling work
Use for:
- lightweight scaffolding helpers
- validation scripts
- link checkers
- template generators
- evidence collectors
- consistency checks

Characteristics:
- must remain subordinate to repo scope
- should be small, explicit, and bounded
- should exist only when they materially improve execution speed, repeatability, or validation

## Rules for agent-created tooling

The agent may create lightweight helper tooling during execution only if all of the following are true:
- the tooling directly supports the current issue or an approved batch of related issues
- manual execution would be repetitive, slow, or error-prone
- the tooling is small, explicit, and bounded
- the tooling does not widen repository scope
- the tooling improves generation, modification, validation, or evidence collection
- the tooling is either ephemeral or clearly placed in an approved location

Do not create:
- agent frameworks
- generalized runtime systems
- plugin architectures
- orchestration infrastructure
- reusable product-like tooling
unless an issue explicitly calls for it and the repo scope is updated accordingly.

## Scope control rules

Stay tightly scoped to the issue.
Do not widen the task casually.

Do not:
- add unrelated files
- rename large parts of the repo without explicit instruction
- introduce framework code just to “make things concrete”
- create new repo sections because they seem generally useful
- inflate a compact doctrine page into a long tutorial

If a task appears to require a larger restructuring, stop and propose the restructuring first.

## Writing rules

Write in a style that is:
- direct
- explicit
- compact
- technical
- high signal

Prefer:
- short sections
- strong headings
- crisp definitions
- clear distinctions
- concrete examples when needed
- architecture diagrams only when they clarify structure or flow

Avoid:
- filler prose
- motivational language
- vague “best practices” phrasing
- marketing tone
- unnecessary repetition
- broad claims without support
- decorative examples

## Doctrine page standard

For doctrine/reference pages, prefer this section shape unless the issue calls for a different structure:

1. Purpose
2. Core claim
3. Definitions
4. Architecture / Mechanics
5. Patterns
6. Anti-patterns
7. Examples
8. Related pages

Not every page must use every section, but pages should feel structurally consistent.

## Standard artifact templates

When creating new artifacts, start from the most relevant template shape.

### Doctrine page template
Use for taxonomy, primers, standards, architecture pages:
- Purpose
- Core claim
- Definitions
- Architecture / Mechanics
- Patterns
- Anti-patterns
- Examples
- Related pages

### Repository standard page template
Use for scope, operating model, page standards:
- Purpose
- Core claim
- Definitions
- Rules / standards
- Exceptions or adaptation rules
- Examples
- Related pages

### Decision record template
Use for architecture or repository decisions:
- Title
- Status
- Context
- Decision
- Rationale
- Consequences
- Related decisions/pages

### README / index template
Use for section entry points:
- Purpose of the section
- What belongs here
- Page index
- Recommended reading order if useful

Do not invent radically different document structures unless there is a clear reason.

## Examples policy

Examples should be:
- minimal
- explicit
- directly tied to the point being made
- easy to scan

Examples are not decoration.
Do not add examples unless they improve understanding.

## Diagram policy

Use diagrams when they clarify architecture, flow, or boundaries.
Prefer simple, maintainable diagrams over elaborate visuals.

Diagrams should:
- reflect actual repository concepts
- match the surrounding terminology
- clarify structure or interaction
- remain compact

Do not add diagrams that merely restate the text in visual form.

## Sources and factual accuracy

When internet access is enabled and the task involves current definitions, model capabilities, tooling behavior, or vendor-specific facts:
- prefer official documentation and primary sources
- prefer current source material over memory
- distinguish stable doctrine from time-sensitive facts

Use external sources for:
- current definitions
- current official capabilities
- current documentation details

Do not use external sources to redefine the repository’s purpose.
Repository purpose and doctrine are local design decisions and must remain consistent with the repo.

## Validation rules

Do not invent build, test, or lint commands if the repository does not define them.

Validation should be proportional to the task.

At minimum:
- verify file paths are correct
- verify links/navigation if touched
- verify the content matches issue scope
- verify terminology is consistent with nearby pages
- verify no unrelated files were changed

If support tooling is created, it must also be validated against the current issue scope.

## Evidence rules

Each implemented issue should produce evidence of work performed.

Evidence should include, as applicable:
- files created
- files modified
- exact deliverables satisfied
- validation performed
- assumptions made
- conflicts or dependency notes
- relevant external references used for time-sensitive material

Evidence does not need to become a permanent repo artifact unless the issue explicitly requires it.
At minimum, include the evidence in the implementation summary or PR-ready summary.

## Parallel execution and conflict rules

Before implementation, determine whether the issue is parallel-safe.

Parallel-safe work typically includes:
- additive doctrine pages in separate paths
- standards pages that do not restructure existing paths
- isolated examples or diagrams for already-defined pages

Conflict-prone work typically includes:
- directory restructuring
- page relocation
- navigation rewrites
- issue batches touching the same README or index files
- changes that redefine canonical terminology or section ownership

Structural work should be planned before additive work that depends on it.

If several issues can be done in tandem, say so explicitly.
If a structural issue creates conflicts, identify it as a blocker or sequencing boundary.

## Issue execution model

Treat issue bodies as the source of truth for:
- Goal
- Deliverable
- Scope
- Done when

If an issue lacks one of these and the task is ambiguous:
- tighten the task first
- propose a plan
- then implement

## Pull request expectations

When preparing work for review:
- keep changes as small as practical
- keep the diff tightly related to the issue
- summarize what changed
- summarize why the structure/content was chosen
- note any assumptions, dependencies, or open questions
- include evidence of implementation and validation

## Safe defaults for this repository

Unless explicitly asked otherwise:
- prefer markdown over code
- prefer reference structure over implementation
- prefer small additive changes over broad rewrites
- preserve existing repo tone and identity
- make one coherent improvement at a time

## Anti-drift reminder

The main failure mode in this repository is drift from doctrine into sprawl.

Before finalizing any change, ask:
- Is this within scope?
- Is this compact?
- Is this reusable?
- Is this clearer than what was there before?
- Does this help both a human reader and an agent?
- Did I create unnecessary tooling or structure?

If the answer to several of these is no, revise the change.
