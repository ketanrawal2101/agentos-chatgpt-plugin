# AgentOS version history

## 0.3.7 — 2026-11-22

- Added a no-retry rule for plan-blocked HeyGen routes and a guarded fallback to direct Avatar Video only when it meets the requested outcome.
- Documented the currently observed 5,000-character direct-avatar script limit.

## 0.3.6 — 2026-11-22

- Made spoken explanations the default for educational videos; silent/music-only exports are incomplete unless requested.
- Added generic HeyGen private-avatar and voice preflight plus narration coverage checks.
- Kept user-specific channel and asset identifiers out of public source files.
- Workflow notes do not train model weights.

## 0.3.5 — 2026-11-22

- Added verified Google Vids educational-motion and voice-source guidance to the video-editor skill and prompt template.
- Added content-free lifecycle reminders to preserve requested video voice fidelity and inspect actual media timing, tracks, and export state.
- Documented pseudo-text, same-scene placement, transition timing, and subtitle-focus lessons from the completed workflow.
- No portraits, voice recordings, video, or transcript are retained; workflow learning does not train model weights.

## 0.3.4 — 2026-11-22

- Added a requirement-first video-editor specialist skill and internal prompt template.
- Added track-specific Google Vids narration alignment and mute-state checks based on the observed workflow.
- Updated orchestration to derive prompts internally, discover available tools, execute requested work, and verify the actual deliverable.
- Updated existing lifecycle hook context for task intake, bounded repair, and completion checks; hooks remain advisory and content-free.
- Added a rollback-aware change record. The GitHub Copilot/VS Code agent profile is maintained separately in the source repository.

## 0.3.3 — 2026-11-22

- Added the reusable `talking-video-agent` specialist skill for portrait/audio/motion-based video production.
- Added motion-aware model selection, cloud upload and credit boundaries, and output quality review.
- Added a required per-install Markdown inventory, full dependency freezes, and uninstall instructions.
- Updated orchestrator and learning governance to maintain evidence-backed skills under the user's explicit standing authorization.
- Clarified that workflow learning does not train model weights and that personal media stays out of training datasets without explicit approval.

