# AgentOS change record — 0.3.4

## Affected behavior

- Adds a video-editor specialist skill for requirement analysis, tool discovery, internal prompt construction, hands-on editing, review, and bounded repair.
- Adds a GitHub Copilot and compatible VS Code custom-agent profile at .github/agents/video-editor.agent.md in the source repository.
- Tightens generic orchestration so the user can describe the desired outcome without selecting the app or writing the model prompt.
- Updates existing lifecycle hook guidance for intake, tool preflight, result observation, repair, and completion.
- Adds a reusable internal production prompt template and video review checks.

## Current behavior and evidence

AgentOS 0.3.3 already includes a talking-video specialist, install inventory guidance, generic bounded workflow loops, and lifecycle hook scripts. The user explicitly requested requirement-first execution. During the Google Vids workflow, the WAV was initially placed after the final scene, and the selected track's Mute control needed to be checked separately for video and narration. These are process observations; no portrait, voice, generated media, or private transcript is retained here.

## Benefit

Reduce avoidable user questions, route video tasks from desired outcome to the right live tool, execute instead of returning only a prompt, and verify the actual timeline and media before reporting completion.

## Risk and compatibility

The custom agent file is recognized only by compatible GitHub Copilot and VS Code hosts. The ChatGPT plugin uses the new skill when selected by the host. Lifecycle hooks remain advisory, static, and content-free; they do not discover tools, observe media, execute edits, persist state, or grant approvals. No permissions, retention, external sharing, or model-training behavior is expanded.

## Rollback

Restore AgentOS release 0.3.3 through Plugin Creator. In the source repository, revert the single versioned change commit or close the associated pull request.
