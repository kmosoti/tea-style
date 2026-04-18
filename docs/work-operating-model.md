# Work Operating Model

## Purpose
Define how work is prepared, executed, reviewed, and closed in `tea-style`.

## Core claim
Work quality in this repository comes from small scoped issues, explicit evidence, and predictable review criteria.

## Definitions
- **DoR (Definition of Ready)**: minimum criteria an issue must meet before implementation starts.
- **DoD (Definition of Done)**: minimum criteria required before an issue can be closed.
- **Evidence type**: artifact class attached to a work item (`Notes`, `Writeup`, `Code`, `Benchmark`).
- **High signal**: content that is precise, reusable, and free of filler.

## Definition of Ready (DoR)
An issue is Ready when all are true:
1. Goal is explicit.
2. Deliverable lists exact file path(s) or artifact(s).
3. Scope boundaries are stated, including out-of-scope items when needed.
4. Done-when criteria are testable.
5. Dependencies and blockers are identified.
6. Pipeline type is classified (A additive, B structural, C support tooling).

## Definition of Done (DoD)
An issue is Done when all are true:
1. Deliverables exist at the declared paths.
2. Content is compact, explicit, and aligned with repository tone.
3. Related links/navigation are updated when affected.
4. Validation is completed (paths, links, terminology consistency, scope checks).
5. Evidence is recorded in issue/PR summary.
6. No unrelated restructuring or scope expansion was introduced.

## Work item sizing
Use small units that can be reviewed quickly:
- **Small**: one page or one focused edit in one area.
- **Medium**: a page plus local cross-link updates.
- **Large**: structural work or changes spanning multiple sections.

Default preference: small or medium. Split large work unless structure changes require a single unit.

## Evidence policy
- **Notes**: durable rough findings captured in issue or comment.
- **Writeup**: polished markdown page(s) committed in repo.
- **Code**: working implementation committed in repo.
- **Benchmark**: measurable comparison artifact with method and result.

Choose the minimum evidence type that proves completion.

## Issue structure standard
Each issue should include:
1. Goal
2. Deliverable
3. Scope
4. Done when

Optional additions: dependencies, blockers, and sequencing notes.


## Project field mapping
When using the TEA Learning Lab project board, set fields explicitly:
- **Status**: `Backlog` -> `Ready` -> `Doing` -> `Review` -> `Done`
- **Track**: `Repo` for governance pages, `Doctrine` for domain doctrine pages, `Experiment` for lab/project pages
- **Evidence**: `Writeup` for markdown doctrine work unless the issue explicitly requires code or benchmark output
- **Difficulty**: numeric estimate used only for sequencing, not quality

For umbrella issues, keep the parent open until child issues are in `Done`.

## Issue linkage rule
Each implementation PR should tie changes to issue numbers in title or body and include a short file-to-issue mapping in the summary.

## PR expectations
- Prefer small, tightly scoped PRs.
- Title should reference the issue or work item.
- Body explains what changed, why, and what was validated.
- For documentation-heavy work, include diagrams/screenshots only when they materially clarify content.

## Decision log rule
Repository-level architecture and doctrine decisions should be recorded under `docs/decisions/` using the decision template defined in that section.

## Review heuristics
Reviewers should ask:
- Is this precise?
- Is this reusable?
- Is this concrete?
- Is this compact enough?
- Does this help both engineers and agents?

## Execution dispatch sheet
Use this bounded dispatch model for parallel work:

### Main agent responsibilities
- clarify scope
- create implementation plan
- make final architecture decisions
- integrate outputs and resolve conflicts

### Subagent responsibilities (bounded)
Spawn subagents only for:
- codebase search and file discovery
- standards/doctrine lookup
- test failure triage
- documentation gap analysis

Each subagent returns only:
- concise findings
- affected files
- recommended actions

Subagents must not make architecture decisions unless explicitly requested.

## Related pages
- `docs/repo-scope.md`
- `docs/page-template-standard.md`
- `docs/examples-and-diagrams-standard.md`
- `docs/decisions/README.md`
