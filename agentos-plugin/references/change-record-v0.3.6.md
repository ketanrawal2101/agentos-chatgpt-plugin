# AgentOS change record — 0.3.6

## Affected behavior

- Makes audible narration the default acceptance condition for lessons, tutorials, explainers, and Q&A videos. A silent or music-only render is incomplete unless the user explicitly requests it.
- Adds generic HeyGen preflight guidance: inspect private avatar and voice assets, use the selected user-owned digital twin and matching active voice directly, and do not substitute public assets.
- Routes long narration-led lessons with B-roll to HeyGen Video Agent; use Avatar Video when exact script/audio preservation or a fixed presenter shot is required.
- Updates lifecycle reminders and media-specific acceptance checks to verify narration for every educational section.

## Evidence

In a completed Google Vids workflow, the generated narration was removed to honor an earlier non-AI-voice request while no human recording was available. The resulting export had music but no spoken explanations. A later HeyGen preflight confirmed that private avatar and voice assets can be checked before production.

## Privacy and compatibility

This public source update contains process guidance only, not user-specific channel details or private asset IDs. Hooks remain advisory and do not inspect media or approve actions. Workflow notes do not train model weights.

## Rollback

Restore the 0.3.5 plugin release or revert the 0.3.6 source changes in the pull request.
