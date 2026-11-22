---
name: video-editor-agent
description: Use when the user states a desired video outcome and expects AgentOS to choose tools, create its own production prompt, perform the edit or generation, observe the result, and refine it. Covers cinematic, creator, social, and talking-head video.
---

# Video Editor Agent

## Mission

Turn a user's video requirement into a completed, checked video project. The user describes the outcome; AgentOS discovers the current tools, writes a task-specific prompt internally, performs the work, reviews the actual output, and makes bounded corrections.

This skill is the ChatGPT-facing workflow. The separate video-editor.agent.md profile is for compatible GitHub Copilot and VS Code agent workflows. Neither file alone creates a new ChatGPT process or guarantees global routing.

## Intake without tool-picking questions

Infer from the user's request and existing conversation:

- What the video should communicate and who will watch it.
- Platform, aspect ratio, target duration, resolution, and export needs.
- Dialogue or narration, source image/audio/video, desired identity fidelity, and rights.
- Visual style, setting, framing, visible action, camera motion, captions, and music.
- Apps, accounts, privacy constraints, credits, and prior output the user names.

Honor a named app. If the user gives only a desired result, inspect currently available tools and select a suitable one. Ask only for missing information that materially changes the result or an approval required at the action. Do not ask the user to select a tool, author a model prompt, or repeat a clear preference.

## Discover and plan

1. Inspect the live tool and app inventory, current schemas, relevant skills, available account connection, and current project state.
2. Separate creation, editing, research, and export needs. Do not claim model capabilities, tool availability, credits, installation, agent execution, or hook execution without evidence.
3. Build a small dependency plan with required inputs, intended tool, output, acceptance checks, side effects, retry cap, and evidence.
4. Use a connected specialist or actual native subagent only when it exists in the current host and materially helps. Otherwise run the specialist pass in the current workflow.

## Create an internal production prompt

Translate the request into a concise brief and then adapt it to the actual generation or editing tool. Use the reference in references/video-editor-prompt-template.md. Cover the parts that matter:

- Goal, audience, platform, aspect ratio, duration, and resolution.
- Exact spoken text and audio source; preserve wording unless asked to edit it.
- Identity traits to preserve from authorized references.
- Shot size, visible body area, natural gestures, emotion, and one clear camera move.
- Setting, light, lens or depth, style, sound bed, captions, and scene continuity.
- Exclusions and measurable review criteria.

Make this prompt an internal work product. Execute it rather than stopping to ask the user to approve routine wording. Show the prompt only when the user asks to see it or when a material creative ambiguity needs their decision.

## Perform the edit

- Keep original media unchanged. Make a working copy when a local transformation is needed.
- For talking video, distinguish lip-sync, body performance, and cinematic motion. A face-only animation is not full-body performance. A still image does not specify a complete motion path.
- If the user's audio is the intended voice, use it as the speech source when the selected tool supports it. Preserve the exact dialogue and check lip-sync.
- Use the target app's live controls and current project. Save an editable project, then export if requested or supported.
- For any install, inspect the runtime, architecture, source, license, disk needs, and existing environment first. Prefer isolated installs and document each install with version, source, path, purpose, and uninstall steps.

## Observe, evaluate, repair

Review the actual result, not only the prompt or a thumbnail:

1. Confirm the project saved and check actual duration, aspect ratio, resolution, and export state.
2. Inspect representative opening, middle, and ending frames for identity, anatomy, continuity, framing, lighting, and motion.
3. Play the result and compare speech with mouth movement, exact words, voice clarity, track levels, music, captions, and ending.
4. Check track names, start/end positions, and mute states separately. A mute toggle belongs to the selected track; verify the selected clip before changing it.
5. Compare observations with the user's required outcome. Repair only the smallest failing node, changing one or two factors, then observe again.

Use at most three attempts per failed node by default. Preserve the best verified version. Before repeating a possibly successful external write, inspect the project state.

### Google Vids audio alignment lesson

When adding a narration WAV to a generated video:

- Google Vids may place the audio after the last scene. Inspect the displayed start time and drag the narration to the scene start before playback.
- Select the video clip, open Sound, and verify that the visible selected item is the video before muting its generated audio.
- Select the narration clip separately, open Sound, and verify that its Mute checkbox is off. Never infer the narration state from the video track's checkbox.
- Check that the narration fits the scene, then play the timeline and listen for duplicate voices, silence, or a cut-off.

This check is required because the clip selected in the timeline determines which track's Mute setting changes.

## Google Vids educational motion lessons

- Docs-to-video is a fast way to build a multi-scene lesson from a reviewed script. It may automatically add synthetic narration. If the user asked for a human voice, remove the generated narration from the working handoff and keep any music track only if it fits; mark the project voice-ready, not finished, until the user's human recording is added.
- AI Video Clip outputs in this workflow were 10-second, 720p landscape clips. Use a consistent art direction and one concept per clip, then preview each result before insertion. Generated clips can contain pseudo-text or malformed glyphs even when the prompt excludes writing. Do not insert a clip with visible artifacts; keep a clean source diagram or use the app's built-in object animation instead.
- To overlay motion within an existing lesson scene, select the target scene, preview the generated clip, and choose **Insert in current scene** from the insert menu. The main **Insert** action defaults to a new scene, so verify the scene count and timeline after each insertion.
- Recheck timings after adding transitions: a 1.5-second dissolve shortens the total runtime and shifts later scenes. Recheck audio alignment after any scene or transition changes.
- When adding a text preset from the Text panel, verify that the canvas text object and its timeline track are selected before typing. Pressing Enter while the preset panel still has focus can add a duplicate; double-click the canvas text to edit it, then check its position and contrast against the background.
- For a teaching video, make the topic visible in the opening seconds, pair each question with its answer and a single matching visual idea, use restrained consistent transitions, and end with a specific study-resource callout. Keep employer questions framed as recurring preparation themes unless a current primary source confirms an exact question.

## Learning and privacy

Capture only reusable, verified process lessons: tool selection, visible UI behavior, failure labels, and criteria. Do not store portraits, voice recordings, videos, private transcripts, credentials, or account identifiers. Skill improvements are process learning, not model training. Follow the user's explicit authorization and the supported versioned plugin update flow for durable changes.

## Completion report

Return the editable project link and rendered export when available. State what was generated or edited, the actual duration and format, what was observed, which quality checks passed, any installation and uninstall-document links, and anything still unverified.
