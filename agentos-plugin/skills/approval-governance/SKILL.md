---
name: approval-governance
description: Use when a workflow includes external writes, publication, messages, purchases, permission changes, deletion, or other consequential side effects.
---

# Approval Governance

## Classify each action

Before execution, mark nodes as read-only, reversible write, externally visible action, or destructive/irreversible action. Use the host's current policy and tool-specific rules to determine the required approval.

## Approval sequence

1. Inspect the tool schema and identify the exact target, data, and side effect.
2. Validate inputs and check for duplicates or prior success.
3. Let the host's approval flow run. If user approval is required outside the tool flow, summarize the concrete action and its target.
4. A denial, cancellation, timeout, or absent authorization stops that action path. Continue unrelated read-only work only when safe.
5. After an approved action, verify the resulting state independently when possible.

## Prohibited shortcuts

Never treat a prior unrelated approval as permission for a new action. Never bypass authentication, workspace policy, provider permissions, or a host confirmation. Never retry an uncertain side effect before checking whether it already succeeded. Delegated agents inherit the same boundaries and cannot grant themselves authority.

