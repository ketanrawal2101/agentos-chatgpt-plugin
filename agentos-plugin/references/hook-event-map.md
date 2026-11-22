# AgentOS Hook Event Map

The hook manifest registers the supported Codex lifecycle event names below. Actual availability depends on the host and execution mode. The script emits static additional context for SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, SubagentStart, and Stop; other events are registered but produce no output.

| Event | AgentOS behavior | Data retained |
|---|---|---|
| `SessionStart` | Reminds the model to treat the request as an outcome and inspect live capabilities | None |
| `UserPromptSubmit` | Reminds the model to analyze the outcome, discover tools, build an internal prompt and checks, and execute | None |
| `PreToolUse` | Adds a static preflight reminder; never approves or blocks a call | None |
| `PermissionRequest` | No-op observer; never approves or denies | None |
| `PostToolUse` | Adds a static result-verification reminder; never retries a call | None |
| `PreModelRequest` / `PostModelRequest` | No-op observer | None |
| `PreCompact` / `PostCompact` | No-op observer; no transcript extraction | None |
| `SubagentStart` | Gives a scoped worker a concise assignment contract | None |
| `SubagentStop` | No-op observer; orchestrator merges verified outputs | None |
| `Stop` | Reminds the model to verify acceptance checks and report the saved deliverable | None |
| `Interrupt` | No-op observer | None |
| `SessionEnd` | No-op observer; no session summary is saved | None |

Hooks are advisory and must not be used as a permission boundary, task executor, quality checker, or durable memory. The model performs tool discovery, editing, and output evaluation. The host's documented configuration and trust requirements control execution. ChatGPT web plugin installation does not deploy command scripts; supported ChatGPT Work/Codex environments can execute bundled plugin hooks when configured and trusted.
