# AgentOS change record — 0.3.5

## Affected behavior

- Adds a reusable Google Vids educational-motion workflow to the video-editor skill: use a reviewed script, add concept-specific short motion inserts, preview every insert for text artifacts, place clips in the intended scene, then recheck transitions and timing.
- Requires preserving the requested voice source. When a user asks for a human voice and the editor auto-generates narration, remove that narration and label the project voice-ready until a human recording is available.
- Adds a prompt-template field for voice source and guidance for fast hooks, question/answer progression, concept-matched motion, captions, and a study-resource ending.
- Extends the existing content-free lifecycle hook reminders for video voice fidelity and actual media review. Existing bounded workflow repair loops remain the execution mechanism; hooks remain advisory.

## Evidence

In a Google Vids learning-video project, Docs-to-video added synthetic narration automatically; the user's requirement was human narration. Removing the generated narration left a voice-ready draft. Short 720p motion inserts were useful for concept scenes, but one preview contained malformed pseudo-text and was excluded. Choosing “Insert in current scene” preserved the scene count. Dissolves changed the total runtime, so timing needed another check. A subtitle preset also retained panel focus and created a duplicate placeholder until it was removed.

## Benefit

Preserves voice-source accuracy, encourages meaningful motion over static slides, and reduces common placement, artifact, and timing errors in educational creator videos.

## Privacy and compatibility

This update contains reusable process guidance only. It does not retain portraits, recordings, transcripts, or rendered video, and it does not train model weights. Hook messages remain static, content-free, and advisory; the current host must support and trust the bundled hook runtime. No permission or sharing scope changes.

## Rollback

Restore the 0.3.4 release from Plugin Creator. In the source repository, revert the 0.3.5 change commit or close its draft pull request. The 0.3.4 skill and change record remain available in release history.
