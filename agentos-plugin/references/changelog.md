# AgentOS version history

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

