# Coding Principles

## Core preferences
- Use Python where it fits the problem.
- Prefer strong typing where it improves clarity.
- Keep modules black-boxed and interfaces narrow.
- Separate configuration from execution logic.
- Use object-oriented structure when it improves consistency and maintainability.
- Prefer modular extension over monolithic growth.
- Prefer dependency injection over hidden construction.
- Prefer protocols and interfaces over inheritance-heavy designs.
- Keep pure logic separate from side-effecting shell code.
- Make invalid states difficult to represent.

## Review standard
Good code should be easy to trace, easy to test, and hard to misuse.

## Tradeoff
Abstraction is useful when it removes repeated decisions. It is harmful when it hides the actual behavior of the system.

## Related pages
- [architecture-boundaries.md](architecture-boundaries.md)
- [docs/doctrines/engineering-control-spine.md](../../docs/doctrines/engineering-control-spine.md)
