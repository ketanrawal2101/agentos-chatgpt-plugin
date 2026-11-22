# Contributing

This repository publishes a source copy of the AgentOS ChatGPT plugin and GitHub Copilot custom agent profiles.

## Keep the runtime boundary clear

- Changes under `agentos-plugin/` are changes to the ChatGPT plugin source package.
- Changes under `.github/agents/` are repository custom agent profiles for compatible Copilot and VS Code hosts.
- A change to one layer does not update or configure the other.
- The installed ChatGPT plugin remains private. Updating this public repository does not publish or reinstall the plugin.

## Change process

1. Identify whether a proposal changes documentation, a custom agent profile, or the ChatGPT plugin source.
2. Keep the change focused and preserve host-specific limitations.
3. For behavior changes, record the affected files, current and proposed behavior, evidence, benefit, risk, compatibility impact, and rollback point.
4. Review activation descriptions and links whenever a skill changes. Review hook event claims against both `hooks/hooks.json` and `hooks/agentos_hook.py`.
5. Verify claims about delegation, approvals, persistence, hook execution, and integrations against the actual host and source.
6. Describe checks that were actually run. Do not report attempts as successful verification.

## Reuse and licensing

The repository currently has no license file. Do not assume that its public visibility grants permission to reuse or redistribute the source.
