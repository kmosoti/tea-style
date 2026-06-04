# Agent Architecture Principles

## Core preferences
- Prefer simple systems before multi-agent expansion.
- Treat context as a design problem, not a dumping ground.
- Keep tool exposure narrow and explicit.
- Evaluate accuracy before scaling complexity.
- Prefer open-source-friendly approaches where practical.
- Let LLMs propose; let deterministic tools verify.
- Keep risky actions behind schemas, policy checks, dry-runs, and human approval.

## Design stance
The goal is not to build the most agentic system. The goal is to build systems that are clean, fast, consistent, and accurate enough to trust.

## Related pages
- [control/deterministic-tool-boundaries.md](control/deterministic-tool-boundaries.md)
- [control/tool-exposure.md](control/tool-exposure.md)
- [evaluation/evals.md](evaluation/evals.md)
