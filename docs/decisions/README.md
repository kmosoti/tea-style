# Decision Log

## Purpose
Record durable repository-level decisions that affect doctrine structure, standards, or canonical terminology.

## What belongs here
Record decisions that change or lock one of the following:
- repository structure or canonical file ownership
- standards that affect multiple pages
- terminology that must stay consistent across domains
- operating model rules used for issue and PR execution

Do not record trivial edits or one-off wording fixes.

## Naming convention
Use sequential filenames:
- `0001-<short-kebab-title>.md`
- `0002-<short-kebab-title>.md`

Keep titles explicit and stable.

## Decision record template
Use this structure:

1. Title
2. Status (`proposed`, `accepted`, `superseded`)
3. Context
4. Decision
5. Rationale
6. Consequences
7. Related pages/decisions

## Minimal decision file example

```md
# 0001-example-decision-title

## Status
accepted

## Context
What problem required a durable decision.

## Decision
What was chosen.

## Rationale
Why this option was selected over alternatives.

## Consequences
Expected tradeoffs and follow-up effects.

## Related pages/decisions
- docs/work-operating-model.md
```

## Usage guidance
- Prefer one decision per file.
- Update status to `superseded` instead of deleting history.
- Link decisions from affected doctrine pages when practical.

## Related pages
- `docs/work-operating-model.md`
- `docs/repo-scope.md`
