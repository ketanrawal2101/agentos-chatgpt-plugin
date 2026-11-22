# AgentOS

AgentOS is a private ChatGPT plugin for coordinating specialist workflow skills, connected tools, bounded task flows, and verification. This repository contains the complete plugin source package.

- **ChatGPT plugin:** [AgentOS](https://chatgpt.com/plugins/plugins_6b02a9f8fea48191abcd3baafd78bf8f)
- **Plugin version:** 0.3.2
- **GitHub repository:** [ketanrawal2101/Ketan-rawal](https://github.com/ketanrawal2101/Ketan-rawal)
- **ChatGPT visibility:** private. This GitHub repository is public, so its source files are public.

## Use AgentOS

For reliable invocation, mention **@AgentOS**. The installed greeting skill is configured so a greeting-only message such as “hello” receives a short AgentOS welcome and stops without delegating, calling tools, or opening connected apps. A greeting that includes a task follows the normal orchestration workflow. ChatGPT controls automatic skill selection, so a plain greeting cannot guarantee exclusive routing across every installed plugin.

## What is included

The plugin contains 20 skills:

- **Orchestration:** coordinator, agent manager, capability discovery, tool routing, workflow engine, workflow evaluator, approval governance, lifecycle hooks, learning governance, versioning, skill factory, and greeting-only behavior.
- **Specialist roles:** research, engineering, quality and security, data analysis, automation, product strategy, creative production, and learning evaluation.

Multi-agent behavior is host-dependent. These specialist skills are role instructions; they become separate parallel workers only when the active ChatGPT host exposes native subagent delegation. AgentOS does not claim to spawn workers when that capability is absent.

## Workflow behavior

For multi-step tasks, AgentOS defines a dependency graph with explicit inputs, outputs, and success checks. It can run independent nodes in parallel when the host supports it. Failed nodes use local, bounded repair loops—three attempts per node by default—and successful work is preserved. Consequential actions follow the host's approval flow and are checked before being reported complete.

## Lifecycle hooks

The package declares 14 lifecycle event hooks. Static guidance is added at session start, prompt submission, before and after tool calls, and subagent start. Remaining event handlers are no-ops; they do not change permissions or approvals. Hook scripts retain no prompts, transcripts, tool arguments, tool results, or credentials.

Hooks require a compatible runtime that can execute and trust the bundled scripts. Installing a plugin on ChatGPT web does not deploy hook scripts; supported ChatGPT Work/Codex hosts may run them after trust review. The hooks are advisory and do not replace host security controls.

## Integrations and privacy

AgentOS does not include a remote MCP server or external agent service. It uses only the tools and connected apps already available in the active ChatGPT conversation. No credentials or conversation data are stored by the plugin hooks.

## Repository layout

```text
agentos-plugin/
├── plugin.json
├── .codex-plugin/plugin.json
├── README.md
├── hooks/
├── references/
└── skills/
```

The public source copy omits the author's email address from plugin metadata. No license file is included; add a license before granting others reuse rights.

