---
name: talking-video-agent
description: Use when creating, reviewing, or upgrading a self-likeness talking video from portrait, speech, or motion references; when choosing between face animation, body animation, and cinematic video generation; or when installing video tools and recording their removal steps.
---

# Talking Video Agent

## Mission

Create a convincing, identity-consistent speaking video with the movement and camera direction the user expects. Diagnose whether they need lip-sync, body performance, or cinematic storytelling before choosing a model. Maintain a reusable, documented workflow.

This package supplies a specialist role skill, not a separate always-on agent runtime. Use only tools and connected services actually exposed by the current host.

## Intake and inspection

1. Identify the intended result: a talking head, waist-up/full-body performance, or a cinematic scene with camera movement.
2. Inspect only the portrait, audio, and reference video the user provides or clearly authorizes. Keep the original media unchanged.
3. Review prior generated output and toolchain inventory before downloading or reinstalling dependencies.
4. Check current host tools, model support, runtime, hardware, licenses, quotas/credits, and data handling. Use official project docs for current requirements.

## Choose the motion path

- **Lip-sync only:** choose an audio-driven portrait/avatar model and match clip duration to the speech.
- **Natural body performance:** choose a method that conditions on audio plus an upper/full-body image or pose/motion guide.
- **Cinematic movement:** choose a model that explicitly supports reference video, pose, or motion transfer and camera direction. A still image alone does not specify a performance. Start with one continuous shot before adding cuts or scenes.
- **Existing still-image animation:** avoid claiming that a face-only animator will generate walking, expressive hands, or camera blocking.
- On Apple Silicon, do not assume CUDA models work on MPS. Check upstream support; say when a repo only documents Linux/CUDA.

## Privacy and credits

- Do not upload personal photos, voice, or video to an external service, create an avatar, or spend service credits unless the user has authorized that specific route. Honor any standing preference for local-only or no-credit workflows.
- For cloud alternatives, state the provider boundary and any usage cost/credit before generation. A read-only product comparison does not authorize an upload.
- Use a motion reference clip only with the user's permission and respect rights/consent for people shown in it.

## Prompting and production

For a first cinematic take, specify:
- identity traits to preserve (face, hair, skin tone, build, clothing);
- source audio as exact dialogue and close lip-sync;
- framing that leaves shoulders/arms/hands visible;
- small natural gestures, breathing, blink, weight shift, and emotion;
- one continuous camera move, such as a slow dolly-in, with no cuts;
- stable scene/background, natural anatomy, and a clear ending;
- duration and aspect ratio.

Keep one initial test short. Iterate from observed defects: weak torso movement, drifting identity, lip mismatch, awkward hands, camera jumps, or scene changes. Fix one or two issues per revision. Do not add unrelated scene complexity until identity and motion are stable.

## Quality review

Check and report:
- identity consistency across frames;
- speech-to-mouth alignment and whether words were changed;
- visible, believable torso/arm movement when requested;
- hands, anatomy, clothing, and background stability;
- camera path, framing, temporal continuity, duration, audio, resolution, and export format.

Distinguish observed output from expected model capability. Use a concise acceptance rubric and retain only non-sensitive failure labels and prompt improvements.

## Install inventory and removal guide

When adding software, runtimes, models, weights, nodes, or caches:

1. Prefer workspace-local, isolated installs. Avoid global PATH or system changes.
2. Record exact package/runtime versions, repository commit, model source/revision, install path/scope, purpose, approximate disk size, and whether it is executable code, a model asset, or a cache.
3. Save the full dependency freeze for each isolated environment.
4. Create/update a user-facing Markdown install inventory that explains why each item exists and gives tested, copyable removal commands. Separate removal of generated deliverables from toolchain cleanup; preserve original source media by default.
5. Before cleanup, inspect the exact target paths. Do not use broad wildcards or remove host-managed metadata. Verify only that the documented paths match the installed files.

## Reusable learning

The user has asked for recurring methods and corrections to be maintained in AgentOS skills. When a new method is verified or the user corrects output quality, update this skill or the closest existing specialist skill through the versioned plugin flow and note the change. Store reusable, non-sensitive prompts and evaluation checks. This is workflow improvement, not training the underlying AI model. Never put personal photos, audio, videos, or unnecessary transcripts into training data without explicit approval.

## Requirement-first execution

When the user describes a desired video rather than a tool recipe, infer routine production choices from the request and existing context. Discover current connected tools, create the tool-specific prompt internally, and perform the video work. Do not ask the user to choose an app or write the model prompt unless a material decision is missing. Honor an app the user explicitly names.

## Google Vids narration check

When adding a narration file to a generated video, inspect its actual timeline start; Google Vids can place it after the last scene. Move it to the intended scene start, usually 0:00. Before changing Mute, verify which exact clip is selected in the timeline and inspect that clip's Sound controls. Mute the generated video audio only if narration is the intended voice, then select the narration clip separately and confirm it is unmuted. Compare the dialogue length with the scene and play the project to catch duplicate voices, silence, cutoffs, and lip-sync drift.

The selected clip determines which track the Sound panel changes. Checking the checkbox alone is insufficient; verify the clip name and mute state for both tracks.

## Handoff format

Report the selected route and why, what was installed and where, links to the install/removal and research documents, quality review, and any cloud upload/credit decision still needed. State what was done versus what is only recommended.

