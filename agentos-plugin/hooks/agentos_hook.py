"""Small, content-free lifecycle context hooks for AgentOS.

The hook reads the event envelope from stdin and never saves prompts,
transcripts, tool arguments, tool outputs, session IDs, or credentials.
It is advisory: host permissions and approval decisions remain authoritative.
"""

from __future__ import annotations

import json
import sys


CONTEXT = {
    "SessionStart": (
        "AgentOS is a workflow skill package. Inspect current tools and permissions. "
        "Treat specialist profiles as instructions; claim separate agents only when "
        "the host actually exposes and runs subagents. Keep retries bounded."
    ),
    "UserPromptSubmit": (
        "Use AgentOS intake and tool discovery for this request. Build a dependency "
        "graph when useful, honor the user's stated constraints, and verify before reporting."
    ),
    "PreToolUse": (
        "Before this tool call, check its declared schema, target, authorization, and "
        "side effects. Preserve the host's approval flow; do not repeat uncertain writes."
    ),
    "PostToolUse": (
        "Inspect the actual tool result against the node's success check. Verify important "
        "side effects independently and check state before retrying an uncertain write."
    ),
    "SubagentStart": (
        "Work only on the assigned specialist scope. Return a concise result with "
        "evidence, uncertainty, and blockers. Avoid overlapping writes and unapproved side effects."
    ),
}


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return

    name = event.get("hook_event_name")
    context = CONTEXT.get(name)
    if not context:
        return

    output = {
        "hookSpecificOutput": {
            "hookEventName": name,
            "additionalContext": context,
        }
    }
    sys.stdout.write(json.dumps(output, separators=(",", ":")))


if __name__ == "__main__":
    main()

