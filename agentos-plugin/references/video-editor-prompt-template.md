# Video Editor Internal Prompt Template

Use this as a planning structure, then adapt it to the current tool's prompt fields. Keep the prompt internal while executing unless the user asks to review it.

## Production brief

- Outcome and audience:
- Platform and delivery:
- Aspect ratio, target duration, and resolution:
- Source assets and permitted use:
- Exact dialogue or narration:
- Identity and reference fidelity:
- Framing and visible body area:
- Performance, gestures, and emotion:
- Setting, lighting, visual style, and camera motion:
- Audio, captions, music, and ending:
- Constraints and exclusions:
- Acceptance checks:

## Prompt construction

Use only authorized references. State what must remain consistent, what the subject should do, how the camera should move, and how the clip should end. Preserve user-provided dialogue exactly. Name unwanted artifacts only when they relate to the requested result. Match the prompt to features the live tool actually supports.

## Review loop

For each unmet acceptance check:

1. Record the observed defect in plain language.
2. Identify the single smallest prompt, edit, or track change likely to fix it.
3. Apply that change within the user's authorization.
4. Recheck the affected frames, audio, timing, and save state.
5. Stop after three attempts for the same failed node and report the remaining limitation.

Do not save private source media or raw transcripts in this template or in reusable skill examples.
