# AgentOS

**A private ChatGPT plugin for task routing, specialist skills, and structured workflows.**

AgentOS helps ChatGPT coordinate complex requests using reusable instructions, connected tools, bounded work loops, and outcome checks. This repository contains a public source copy of the plugin package. It is not a standalone AI product or hosted agent service.

## What it includes

- **22 reusable skills** for orchestration, tool discovery, specialist work, workflow planning, quality review, learning, and video production.
- **A greeting-only skill** designed to keep a simple hello brief. For explicit routing, mention **@AgentOS**; ChatGPT still controls automatic skill selection.
- **Requirement-first video editing**: AgentOS can infer a production prompt from a requested outcome, choose from currently available tools, perform the edit, inspect the result, and make bounded repairs.
- **Workflow guidance** that maps multi-step work into dependencies, allows parallel steps when the host supports them, and uses bounded repair loops.
- **Lifecycle hook definitions** for compatible runtimes. Hooks are advisory and do not replace host approval or security controls.
- **Ten custom agent profiles** for GitHub Copilot and compatible VS Code workflows, stored in [.github/agents/](./.github/agents/). These profiles are separate from the ChatGPT plugin skills.

## Use with ChatGPT

The ChatGPT plugin is private to its owner and is not publicly installable. For dependable use in a conversation, mention **@AgentOS**. A plain greeting cannot guarantee that ChatGPT will select AgentOS over every other installed plugin.

AgentOS provides specialist role instructions; separate parallel agents are available only when the active host provides native subagent delegation. Hook scripts require a compatible runtime and trust review. Installing the plugin in ChatGPT web does not install or run those scripts.

## Repository layout

The complete plugin package is in [agentos-plugin/](./agentos-plugin/), including its manifests, skills, hook definitions, and references. See the [package README](./agentos-plugin/README.md) for details.

Repository custom agents are in [.github/agents/](./.github/agents/). See the [documentation index](./docs/README.md) for architecture, compatibility, workflows, and skill-to-agent mapping.

## Privacy and integrations

AgentOS uses the tools and connected apps already available in the active ChatGPT conversation. It does not include a remote MCP server or external agent service. Its hooks do not retain prompts, transcripts, tool arguments, tool results, or credentials. Workflow skill updates improve instructions; they do not train model weights.

## License

No license is included. Please contact the author before reusing or redistributing this source until a license is added.
