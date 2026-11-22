# Workflow Graphs and Repair Loops

For multi-step requests, AgentOS uses a dependency graph so each step has a clear purpose and a verifiable result.

## Requirement-first execution

1. Read the user's requested outcome, constraints, deliverable, and any named app.
2. Discover current tools, connected apps, skills, schemas, and permissions. Honor a named app; otherwise choose a suitable available tool.
3. Construct a task-specific internal prompt or production brief and acceptance checks. Do not ask the user to write a prompt or pick a tool when the request is clear.
4. Perform the requested work when the host exposes a suitable capability.
5. Observe the actual artifact or app state and evaluate it against the checks.
6. Repair the smallest failing step within the per-node retry cap, then verify again.
7. Save and link the completed deliverable; separate completed work from recommendations and unknowns.

## Node contract

A workflow node should define:

- Objective and required inputs
- Dependencies and selected role or tool
- Expected output and a success predicate
- Side-effect class and approval requirement
- Evidence to collect and a retry cap

Independent nodes may run in parallel only when the active host supplies real parallel or subagent support. Steps that share files or depend on earlier results stay coordinated.

## Bounded repair

When a node fails, inspect the actual result, compare it with the success predicate, classify the cause, and repair the smallest affected node. The default cap is three attempts per node. Preserve successful nodes and rerun descendants only when their inputs became stale.

Before retrying an uncertain external write, inspect whether it already succeeded. Stop on denied approval or missing authorization. Never retry indefinitely.

## Media-specific acceptance checks

For educational video nodes, require audible explanations unless the user requests no narration. Check the saved project, export dimensions and duration, representative opening/middle/ending visuals, selected voice and avatar, audio-track alignment, captions, and spoken call to action. Preview generated inserts for malformed text or artifacts; verify they were placed in the intended scene. Recheck runtime after transitions or scene edits. Record unverified playback/export states and keep repairs within the existing per-node retry cap.

## State reference

The detailed states and invariants are in [workflow-state-machine.md](../agentos-plugin/references/workflow-state-machine.md). In brief: plan, check preconditions, execute, observe, evaluate, repair if needed, then mark passed only when evidence meets the check.

The graph and retry loop are instructions; actual state persistence and parallel execution depend on the host.
