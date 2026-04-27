# Agent Architecture

This domain captures how I want to reason about agent systems without turning them into hype objects.

The emphasis is on context management, retrieval discipline, tool boundaries, evaluation, operational clarity, and controlled implementation inside tools such as VS Code GitHub Copilot Chat.

This is a doctrine in progress rather than a claim of mastery.

## Core pages
- `principles.md`
- `research/vscode-copilot-agentic-workflow-research.md`
- `standards/agentic-ai-design-standard.md`
- `workflows/vscode-copilot-handoff-hierarchy.md`
- `templates/copilot-handoff-hierarchy-templates.md`

## Existing sections
- `concepts/` - core agent architecture concepts
- `patterns/` - reusable agent design patterns
- `rag/` - retrieval and knowledge-injection doctrine
- `standards/` - review, documentation, and design standards
- `models/` - model taxonomy and inference mechanics doctrine
- `projects/` - bounded practice projects for agent architecture skills

## Design stance
Use the lightest reliable pattern.

The preferred progression is:

1. deterministic program
2. single model call
3. retrieval-supported answer
4. tool-using agent
5. custom agent
6. multi-agent workflow

Do not skip to multi-agent orchestration unless the role boundaries, tool boundaries, and evaluation path are clear.
