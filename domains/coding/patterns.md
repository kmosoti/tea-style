# Coding Patterns

## Preferred patterns
- configuration objects passed into execution code
- value objects and typed models instead of loose dictionaries
- factories when object construction needs to stay consistent
- composition over inheritance when behavior can be assembled cleanly
- focused modules with one obvious responsibility
- protocols for behavior contracts
- functional core with imperative shell
- command/query separation for safer review
- explicit error taxonomy and result objects

## Design target
Code should expose a small public surface and keep orchestration logic readable.
