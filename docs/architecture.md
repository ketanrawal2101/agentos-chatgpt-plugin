# AgentOS Architecture

## Two distinct layers

### ChatGPT plugin package

The installable plugin source is in [agentos-plugin/](../agentos-plugin/). It contains:

- `plugin.json` manifests and the skills directory
- 20 reusable `SKILL.md` workflows
- A hook manifest and a small content-free command hook
- Two reference documents for hook events and workflow states

The plugin is an instruction package for ChatGPT hosts. This repository does not include a hosted agent service, a standalone application, or a remote MCP server.

### Repository custom agents

The repository's `.github/agents/*.agent.md` files define custom profiles for GitHub Copilot and compatible VS Code workflows. They help those hosts select a focused prompt for repository work. They are separate from the ChatGPT plugin package and are not loaded by `@AgentOS`.

## Skills and agents serve different jobs

A skill is a reusable workflow instruction selected for a matching task. A custom agent profile gives a compatible host a named role and prompt. A skill can support several agents; governance and routing skills can remain shared instructions without needing their own agent profile.

## Runtime boundaries

- The active host determines available tools, app connections, approvals, and native subagent support.
- A specialist profile is not proof that a separate worker was launched.
- The hook manifest can declare events that a host does not support or execute.
- Hooks are advisory and do not replace host permissions.
- The installed plugin does not persist conversation state.

See [host compatibility](host-compatibility.md) before claiming a capability.
