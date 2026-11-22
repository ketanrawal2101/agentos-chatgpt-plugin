# Host Compatibility

AgentOS is packaged for ChatGPT plugin hosts. This repository also contains custom agent profiles for GitHub Copilot and compatible VS Code workflows. Those are different runtime formats.

## ChatGPT plugin

The directory `agentos-plugin/skills/` contains the plugin's 20 `SKILL.md` workflows. ChatGPT decides when to select skills; explicitly mention `@AgentOS` when direct routing matters. A plain greeting cannot guarantee exclusive selection over other installed plugins.

AgentOS contains role instructions, but separate parallel workers require native subagent support from the active host. The plugin does not ship a separate agent runtime.

The plugin's command hooks require a host that supports and trusts those scripts. Installing the plugin on ChatGPT web does not deploy the bundled commands. Check the current host and hook support before claiming execution.

## GitHub Copilot and VS Code

Repository custom agents live in `.github/agents/` as `.agent.md` Markdown files with YAML frontmatter. GitHub documents this location for repository custom agents; VS Code also recognizes workspace agent files. Runtime fields and delegation behavior depend on the selected harness.

The profiles in this repository do not grant new tool permissions. A host supplies the tools, and its own policy controls what those tools can do. The profile text is guidance, not a security boundary.

## OpenAI API agents

The source package does not configure an OpenAI Agents API session or enable multi-agent orchestration. The Agents API requires a session configured with multi-agent support; see [OpenAI's multi-agent guide](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).

## References

- [OpenAI plugin skills](https://developers.openai.com/plugins/concepts/skills)
- [GitHub custom agents](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents)
- [VS Code custom agent file reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)
