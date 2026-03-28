# Agent Architecture Principles

## Intent
This section captures how I prefer agent based systems to be structured.

## Core preferences
- Agent systems should have clear boundaries and responsibilities.
- Tools should be explicit, narrow, and easy to reason about.
- Context should be curated rather than bloated.
- Orchestration should remain understandable under failure.
- Agent behavior should be constrained by contracts and validation.

## What good looks like
- Clear separation between planner, executor, and tool layers when needed
- Typed or otherwise validated boundaries
- Observable execution paths
- Minimal hidden state
- Reusable domain specific tooling

## What to avoid
- One giant agent prompt pretending to be architecture
- Undefined tool boundaries
- Context sprawl
- Silent failure modes
- Magical autonomy without verification
