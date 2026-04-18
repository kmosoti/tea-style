# Examples and Diagrams Standard

## Purpose
Define when examples and diagrams should be used so doctrine stays concrete without becoming noisy.

## Core claim
Examples and diagrams are explanatory tools. They are included only when they reduce ambiguity or improve execution.

## Definitions
- **Useful example**: minimal example that directly clarifies a claim, pattern, or tradeoff.
- **Decorative example**: example that repeats text without adding decision value.
- **Useful diagram**: compact visual that clarifies boundaries, flow, or architecture mechanics.

## Rules for examples
Include an example when a concept is abstract enough that text alone may be misread.

A valid example must be:
- minimal
- explicit
- directly tied to the point being made
- easy to scan

Avoid examples that are:
- generic filler
- marketing-style scenarios
- large pseudo-projects that widen scope

## Minimal example structure
When used, examples should usually include:
1. Context
2. Preferred shape
3. Why this shape is preferred

## Rules for diagrams
Include a diagram when it clarifies one of:
- architecture boundaries
- data/control flow
- lifecycle or sequencing

Diagrams must:
- map to real repository concepts and terms
- stay compact and maintainable
- be kept in sync with surrounding text

Do not include diagrams that merely restate prose or add visual noise.

## Diagram types and notation
Preferred formats:
- Mermaid for lightweight in-repo diagrams
- compact text diagrams when they are clearer than graphical forms

Preferred types:
- flowcharts for process flow
- boundary/component diagrams for ownership and interfaces
- sequence-style diagrams for interaction order

## Quality checks
Before finalizing a page with examples/diagrams, verify:
- each artifact answers a concrete ambiguity
- each artifact has a clear relationship to surrounding claims
- deleting the artifact would reduce clarity

## Related pages
- `docs/page-template-standard.md`
- `docs/writing/technical-writing-standards.md`
- `docs/diagrams/diagramming-standards.md`
