---
name: tool-router
description: Use when AgentOS must choose among available tools, connected apps, plugins, or skills for a workflow node and safely route each action.
---

# Tool Router

## Route from the live session

1. Identify the task's required input, output, freshness, and side effects.
2. Inspect current tool and skill declarations. Check the exact schema, connection state, permissions, approval behavior, and returned evidence.
3. Keep these states separate: listed, installed, connected, authenticated, callable, and authorized for the requested action.
4. Rank eligible tools by task fit, permission/data boundary, verification quality, source authority, reliability, then latency/cost.
5. Assign one tool to each graph node and state why it fits. Use the smallest set that can complete the task.

## Execution

- Follow declared schemas exactly; do not invent parameters or endpoints.
- Prefer read-only inspection before writes.
- Validate the target and arguments before a consequential call.
- Respect approval prompts and permission denials. A tool's presence is not authorization.
- Use idempotency or duplicate checks when available. If a write times out, inspect current state before retrying.
- Verify important writes through an independent read when possible.

## Fallback

If a tool is unavailable, identify the precise gap. Choose a fallback only when it meets the same permission and data requirements. Do not silently send data to a different provider or change the task's side effects. If no safe fallback exists, preserve completed work and report the blocker.

