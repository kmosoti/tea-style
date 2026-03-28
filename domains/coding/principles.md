# Coding Principles

## Intent
This section captures how I prefer code to be designed and evaluated.

## Core preferences
- Strong typing should clarify behavior, not decorate it.
- Interfaces matter more than concrete implementations.
- Encapsulation should reduce cognitive load.
- Configuration and execution should be separated.
- Code should be explicit enough to review without guesswork.

## What good looks like
- Narrow public interfaces
- Clear data models
- Deterministic behavior
- Focused functions and classes
- Tests around important logic

## What to avoid
- Loose dictionaries where models should exist
- Hidden side effects
- Overly clever abstractions
- Architecture that is harder to understand than the problem
