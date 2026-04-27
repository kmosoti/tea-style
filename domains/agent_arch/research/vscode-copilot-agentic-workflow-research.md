# VS Code Copilot Agentic Workflow Research

## Purpose
Capture the research base for designing agentic AI workflows in Visual Studio Code with GitHub Copilot Chat.

This is a knowledge-base page. It is not an active Copilot configuration file.

## Primary sources

- Karpathy Autoresearch repository: https://github.com/karpathy/autoresearch
- Karpathy Autoresearch program: https://github.com/karpathy/autoresearch/blob/master/program.md
- Karpathy LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- GitHub awesome-copilot repository: https://github.com/github/awesome-copilot/tree/main
- VS Code Copilot customization overview: https://code.visualstudio.com/docs/copilot/customization/overview
- VS Code Copilot custom instructions: https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- VS Code Copilot custom agents: https://code.visualstudio.com/docs/copilot/customization/custom-agents
- VS Code Copilot agent skills: https://code.visualstudio.com/docs/copilot/customization/agent-skills
- VS Code Copilot planning: https://code.visualstudio.com/docs/copilot/agents/planning
- VS Code Copilot memory: https://code.visualstudio.com/docs/copilot/agents/memory
- VS Code Copilot context engineering guide: https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide
- VS Code Copilot Chat repository: https://github.com/microsoft/vscode-copilot-chat/tree/main

## Implementation reference links

- Workspace instructions reference: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/skills/agent-customization/references/workspace-instructions.md
- Instructions reference: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/skills/agent-customization/references/instructions.md
- Agents reference: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/skills/agent-customization/references/agents.md
- Skills reference: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/skills/agent-customization/references/skills.md
- Create agent prompt: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/create-agent.prompt.md
- Create instructions prompt: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/create-instructions.prompt.md
- Create skill prompt: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/create-skill.prompt.md
- Init prompt: https://github.com/microsoft/vscode-copilot-chat/blob/main/assets/prompts/init.prompt.md

## awesome-copilot references

- Agents instruction standard: https://github.com/github/awesome-copilot/blob/main/instructions/agents.instructions.md
- Agent skills instruction standard: https://github.com/github/awesome-copilot/blob/main/instructions/agent-skills.instructions.md
- Documentation sync instruction: https://github.com/github/awesome-copilot/blob/main/instructions/update-docs-on-code-change.instructions.md
- Polyglot test planner agent: https://github.com/github/awesome-copilot/blob/main/agents/polyglot-test-planner.agent.md
- Polyglot test implementer agent: https://github.com/github/awesome-copilot/blob/main/agents/polyglot-test-implementer.agent.md
- Polyglot test tester agent: https://github.com/github/awesome-copilot/blob/main/agents/polyglot-test-tester.agent.md
- Rug orchestrator agent: https://github.com/github/awesome-copilot/blob/main/agents/rug-orchestrator.agent.md
- Remember skill: https://github.com/github/awesome-copilot/blob/main/skills/remember/SKILL.md
- Memory merger skill: https://github.com/github/awesome-copilot/blob/main/skills/memory-merger/SKILL.md

## Core extraction

The strongest pattern is not autonomous swarm behavior. The stronger pattern is a layered customization stack:

1. Repository instructions define stable project-wide norms.
2. Scoped instructions define path-specific or task-specific behavior.
3. Custom agents define role behavior and tool access.
4. Skills define reusable procedures.
5. Planning and memory preserve task state and durable knowledge.

The doctrine for `tea-style` is: **instructions first, agents second, memory third**.

## Karpathy extraction

The transferable principles from Autoresearch are:

- baseline first
- bounded mutability
- immutable evaluator
- keep-or-discard decisions based on measured output
- persistent result logging
- treating the instruction layer as a reviewed artifact

The transferable principles from the LLM Wiki gist are:

- separate raw sources, synthesized knowledge, and schema
- maintain high-signal knowledge pages
- periodically lint the knowledge base
- preserve useful answers as artifacts

## Repository mapping

| Finding | Repo destination |
|---|---|
| Source links and extracted findings | this page |
| Design doctrine | `domains/agent_arch/standards/agentic-ai-design-standard.md` |
| VS Code workflow | `domains/agent_arch/workflows/vscode-copilot-handoff-hierarchy.md` |
| Copyable templates | `domains/agent_arch/templates/copilot-handoff-hierarchy-templates.md` |
