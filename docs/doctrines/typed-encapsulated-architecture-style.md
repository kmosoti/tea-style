# Typed Encapsulated Architecture Style

Typed Encapsulated Architecture Style (TEA Style) is a software engineering doctrine for building systems that are strongly typed, configuration-driven, and implementation-agnostic.

The premise is simple: code defines the structure, constraints, and interfaces of a system. Tools such as GitHub Copilot or other agents may accelerate implementation, but they operate inside those constraints rather than replacing them.

## Core principles

### 1. Separate configuration from execution
Borrowing from Salt's pillar and state philosophy, TEA separates static data from execution logic.

- Configuration should live in explicit sources such as YAML, JSON, environment variables, or typed settings classes.
- Configuration should be validated at boundaries before business logic runs.
- Execution code should consume validated objects, not loose dictionaries or partially trusted input.

### 2. Program to contracts
Use abstract base classes, protocols, or equivalent interfaces to define behavior.

- Callers depend on contracts.
- Implementations remain replaceable.
- Orchestration code should not couple itself to internal details.

### 3. Treat components as black boxes
Each module should expose a narrow public surface.

- Inputs are explicit.
- Outputs are explicit.
- Internal behavior stays private unless there is a genuine reuse case.

### 4. Use typing as architecture
Type hints are not decoration. They are part of the design.

- Prefer explicit models over generic dictionaries.
- Make return types and failure modes legible.
- Use static analysis to catch drift before runtime.

### 5. Keep logic heavy and data blind
Operational classes should derive behavior from validated inputs and stable contracts.

- Avoid embedding configuration lookup deep inside execution logic.
- Avoid hidden side effects where possible.
- Push environment-specific data to the boundaries.

### 6. Use AI under constraint
AI tools are accelerators, not authorities.

- Let agents propose and implement.
- Keep interfaces, tests, and validation as the source of truth.
- Prefer deterministic guardrails over prompt optimism.

## Operational rules

1. Validate configuration before execution.
2. Prefer interfaces over concrete coupling.
3. Keep modules narrowly scoped.
4. Enforce deterministic formatting.
5. Enforce static typing.
6. Write docstrings and signatures that make intent unambiguous.
7. Require tests for important behavior.

## Recommended workflow

1. Define the data model.
2. Define the interface.
3. Define tests and validation criteria.
4. Let the implementation follow the contract.
5. Use agents to speed up execution, not to invent architecture.
6. Refactor only after behavior is proven.

## What TEA is not

- It is not a ban on pragmatism.
- It is not type maximalism for its own sake.
- It is not blind trust in frameworks or AI tools.
- It is not architecture astronautics.

The standard is simple: strong boundaries, explicit contracts, low ambiguity, and tools that remain subordinate to design.
