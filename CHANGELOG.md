# Changelog

## 2026-11-22 — AgentOS 0.3.6 narration-first video workflow

- Made narration a default acceptance condition for educational videos and added HeyGen private avatar/voice preflight guidance.
- Updated the video-editor skill, compatible agent profile, media acceptance loops, hooks, and rollback record.
- User-specific channel and HeyGen asset identifiers remain in the private plugin profile, not in public source.

## 2026-11-22 — AgentOS 0.3.5 educational video workflow

- Added Google Vids motion-production lessons, human voice-source fidelity, and scene/timing review to the video-editor skill and agent profile.
- Updated the existing advisory lifecycle hook script and media-specific loop guidance; no private media is stored and no model weights are trained.
- Added a versioned change record and rollback instructions.

## 2026-11-22 — AgentOS 0.3.4 video editor workflow

- Added a dedicated video-editor.agent.md profile for compatible GitHub Copilot and VS Code workflows.
- Synchronized the plugin source with the installed 0.3.3 release and advanced the package to 0.3.4.
- Added the video-editor-agent skill, internal prompt template, Google Vids audio-track checks, bounded review loop, hook guidance, and rollback record.
- Hooks remain advisory and content-free; skill changes do not train model weights.

## 2026-11-22 — Repository documentation and custom agents

- Added nine repository custom agent profiles under .github/agents/ for compatible GitHub Copilot and VS Code workflows.
- Added architecture, host compatibility, workflow, and skill-to-agent mapping documentation.
- Expanded the root README with clear links to the profiles and documentation.
- Corrected the hook event reference to match the hook script's context-producing events.
- No ChatGPT plugin runtime behavior, installed plugin version, or hook implementation changed in that earlier update.
