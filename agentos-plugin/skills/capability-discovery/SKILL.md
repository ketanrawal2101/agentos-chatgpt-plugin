---
name: capability-discovery
description: Use when selecting tools for a request, auditing available integrations, discovering a newly connected app, checking tool compatibility, or refreshing AgentOS capability knowledge.
---

# Capability Discovery and Routing

## Discovery procedure
1. Inspect the current session's available tool declarations and relevant installed skill catalog. Use the exact live names and schemas.
2. For each candidate, identify supported actions, input/output schema, authentication/connection state if exposed, read/write scope, runtime availability, and approval requirements.
3. Check relevant first-party marketplace or provider documentation when a capability is new, changing, unclear, or requested by the user.
4. Distinguish: discoverable, installed, connected/authenticated, callable in this runtime, and authorized for this action. These are separate states.
5. Select the smallest set of capabilities that can complete the task. Prefer direct native functionality over redundant integrations.
6. If no suitable capability is available, state the precise gap and offer a viable supported path. Never invent an endpoint or claim that a tool is connected.

## Routing score
Rank candidates using, in order: task fit and schema compatibility; permission and data-boundary fit; reliability and verification; freshness/authority of data; latency/cost; user preference. A tool that cannot satisfy the required schema or permission boundary is ineligible regardless of score.

## Capability record
Maintain records only when the runtime supports persistent storage. Suggested fields:
`provider`, `tool_name`, `description`, `actions`, `input_schema_ref`, `output_schema_ref`, `runtime`, `connection_state`, `permission_scope`, `risk_class`, `verification_method`, `source`, `last_checked_at`, `status`.
Do not copy credentials, tokens, secrets, or sensitive personal data into the registry.

## Refresh and drift
Re-inspect the live catalogue when a task depends on a capability, after a connection change, or when a tool fails unexpectedly. Mark stale records as unverified. A new marketplace listing is not automatically installed, connected, authenticated, or authorized.

## Fallback
If the preferred tool is unavailable, try another candidate only if it meets the same data, permission, and output requirements. Do not silently substitute a tool that sends data to a different provider or changes the side effects.

