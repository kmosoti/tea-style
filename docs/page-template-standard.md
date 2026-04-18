# Page Template Standard

## Purpose
Provide a predictable section template for doctrine/reference pages across the repository.

## Core claim
A shared page shape improves consistency and makes pages easier for both engineers and agents to use.

## Definitions
- **Doctrine page**: a standards, taxonomy, pattern, or architecture reference page.
- **Required section**: section expected in nearly all doctrine pages.
- **Optional section**: section included only when it improves clarity.

## Standard template
Use this order by default:
1. Purpose
2. Core claim
3. Definitions
4. Architecture / Mechanics
5. Patterns
6. Anti-patterns
7. Examples
8. Related pages

## Required vs optional
### Required sections
- Purpose
- Core claim
- Definitions
- Related pages

### Optional sections
- Architecture / Mechanics
- Patterns
- Anti-patterns
- Examples

Optional sections should be omitted when they add no signal.

## Adaptation rules
Adapt the template when page type requires it:
- Repository standards pages may use: `Rules / standards`, `Exceptions`, `Examples`.
- Decision records should use the decision record template under `docs/decisions/README.md`.
- README/index pages should focus on: purpose, what belongs here, page index, reading order.

Do not reorder sections arbitrarily; keep the structure stable unless a page type explicitly calls for a different shape.

## Usage guidance
Apply this template to new doctrine/reference pages first. Existing legacy pages can be aligned incrementally when touched by scoped work.

## Related pages
- `docs/writing/technical-writing-standards.md`
- `docs/examples-and-diagrams-standard.md`
- `docs/decisions/README.md`
