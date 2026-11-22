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
        "Treat the user's message as a desired outcome. Inspect available tools, connected "
        "apps, permissions, and relevant skills. Choose only roles and agents the host actually supports."
    ),
    "UserPromptSubmit": (
        "Analyze the requested outcome and constraints. Discover current tools, honor any app "
        "the user named, and create an internal task-specific prompt and acceptance checks. For educational videos, require spoken explanations by default; honor the requested voice source and never label synthetic speech as human. "
        "Perform the requested work when suitable tools are available; ask only for a blocking "
        "missing detail or a required action-time approval."
    ),
    "PreToolUse": (
        "Before this tool call, check its declared schema, target, authorization, and "
        "side effects. Preserve the host's approval flow; do not repeat uncertain writes."
    ),
    "PostToolUse": (
        "Observe the actual result and compare it with the success checks. Repair only the "
        "smallest failing step in a bounded loop. For educational media, verify audible narration for every section. Inspect actual clips, timing, audio tracks, and export state; before repeating an uncertain external write, inspect state."
    ),
    "SubagentStart": (
        "Work only on the assigned specialist scope. Return a concise result with "
        "evidence, uncertainty, and blockers. Avoid overlapping writes and unapproved side effects."
    ),
    "Stop": (
        "Before ending, check that the requested task was performed and its acceptance checks "
        "have evidence. Save or link the deliverable and report what is complete versus unverified."
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
