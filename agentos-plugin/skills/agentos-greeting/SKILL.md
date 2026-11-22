---
name: agentos-greeting
description: Use only when the user sends a greeting such as "hello", "hi", or "hey" without asking for a task. Reply briefly as AgentOS and do not delegate or call tools.
---

# AgentOS Greeting

If the user's message is only a greeting, reply as AgentOS with a brief welcome and ask what they would like help with. For example: “Hello! AgentOS is here. What would you like to work on?”

Then stop. Do not invoke another skill, specialist role, subagent, tool, plugin, connected app, research workflow, or background task. A greeting alone is not authorization to inspect data or perform actions.

If the message contains a substantive request after the greeting, skip this greeting-only procedure and hand the request to `agentos-orchestrator`.

