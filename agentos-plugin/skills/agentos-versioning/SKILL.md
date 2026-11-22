---
name: agentos-versioning
description: Use when proposing or applying changes to AgentOS skills, hook behavior, role definitions, routing policies, or other versioned plugin instructions.
---

# AgentOS Versioning and Rollback

## Change record

For each proposed change, record the affected file, current and proposed behavior, evidence, expected benefit, risk, compatibility impact, and rollback point. Keep the change focused.

## Review gates

1. Confirm the change addresses a repeated or well-evidenced need; one unusual failure is not a pattern.
2. Check for conflicts with higher-priority system, user, and host instructions.
3. Review skill activation descriptions for overlap and verify references resolve.
4. Review hook edits for supported events, trust behavior, data collection, and surface limitations.
5. Compare against prior successful workflows and current acceptance criteria.
6. Require explicit user authorization for changing permissions, data retention, external sharing, publication, or consequential side-effect behavior.

## Promote and roll back

Never edit or publish the plugin automatically from a normal workflow. Present a concrete change for the user's explicit approval through the supported plugin update process. Preserve the previous release ID and a reversible update path. If a regression appears, stop using the affected procedure and restore the last known-good version through the host's release/update controls.

## Persistence boundary

AgentOS skills do not automatically rewrite themselves and do not provide cross-session database memory. Keep proposals in the current conversation unless a durable store is explicitly available and authorized.

