# Typed Encapsulated Architecture Style

Typed Encapsulated Architecture Style is a doctrine for building systems that are explicit, modular, reviewable, and durable.

## Core ideas
- Prefer strong typing where it clarifies behavior.
- Keep modules black-boxed with narrow public interfaces.
- Separate configuration from execution.
- Prefer maintainable object-oriented structure where it improves consistency.
- Use abstract factories and interface-driven design when they reduce drift across implementations.
- Keep dependencies lean.
- Prefer understandable code over clever code.

## Design stance
TEA is not a framework. It is a decision style.

It pushes work toward:
- validated inputs
- constrained side effects
- explicit contracts
- modular extension paths
- predictable review

## What TEA rejects
- architecture by novelty
- hidden global behavior
- configuration embedded deep inside logic
- abstractions without a real pressure behind them
- dependency growth without clear value

## Standard question
When evaluating a design, the basic question is:

Does this make the system easier to understand, safer to extend, and easier to review?

If not, the complexity likely does not belong.
