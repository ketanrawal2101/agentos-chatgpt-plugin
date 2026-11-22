# AgentOS Hook Event Map

The hook manifest registers the supported Codex lifecycle event names below. Actual availability depends on the host and execution mode. The script emits static additional context for `SessionStart`, `UserPromptSubmit`, and `SubagentStart`; other events are registered but produce no output.

| Event | AgentOS behavior | Data retained |
|---|---|---|
| `SessionStart` | Reminds the model to inspect live capabilities and avoid claiming unspawned agents | None |
| `UserPromptSubmit` | Reminds the model to intake the current task and verify completion | None |
| `PreToolUse` | Adds a static preflight reminder; never approves or blocks a call | None |
| `PermissionRequest` | No-op observer; never approves or denies | None |
| `PostToolUse` | Adds a static result-verification reminder; never retries a call | None |
| `PreModelRequest` / `PostModelRequest` | No-op observer | None |
| `PreCompact` / `PostCompact` | No-op observer; no transcript extraction | None |
| `SubagentStart` | Gives a scoped worker a concise assignment contract | None |
| `SubagentStop` | No-op observer; orchestrator merges verified outputs | None |
| `Stop` / `Interrupt` | No-op observer | None |
| `SessionEnd` | No-op observer; no session summary is saved | None |

Hooks are advisory and must not be used as a permission boundary. The host's documented configuration and trust requirements control execution. ChatGPT web plugin installation does not deploy command scripts; supported ChatGPT Work/Codex environments can execute bundled plugin hooks when configured and trusted.

