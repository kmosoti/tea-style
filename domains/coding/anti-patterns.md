# Coding Anti-Patterns

## Reject
- configuration lookup scattered throughout business logic
- giant utility files with unrelated helpers
- implicit contracts hidden in comments
- abstraction layers that exist only to sound sophisticated
- dependency sprawl for small gains
- dynamic structures where typed models should exist
- mutation hidden behind read-like names
- temporal coupling that requires undocumented call order
- raw external API shapes leaking into core logic
- catch-all exceptions that erase failure policy

## Signal of a problem
If reading a file forces a reviewer to guess state, control flow, or valid inputs, the design is already slipping.
