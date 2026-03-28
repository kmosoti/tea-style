# Automation Principles

## Intent
This section captures how I prefer automation, configuration management, and platform workflows to be designed.

## Core preferences
- Automation should reduce ambiguity and repeated manual effort.
- Configuration should be a source of truth, not scattered state.
- Workflows should be observable and recoverable.
- Safety matters more than cleverness.
- Operational logic should be structured for maintenance, not just initial success.

## What good looks like
- Idempotent behavior where possible
- Clear separation of config, execution, and orchestration
- Failure states that can be diagnosed
- Low drift between intended and actual state
- Reusable building blocks

## What to avoid
- Hidden dependencies
- Snowflake operational logic
- Over coupled workflows
- Automation that cannot be debugged
- Manual tribal steps disguised as process
