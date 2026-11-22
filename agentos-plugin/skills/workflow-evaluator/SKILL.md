---
name: workflow-evaluator
description: Use to define acceptance criteria, review specialist or tool outputs, score workflow results, and decide whether a node passed, needs repair, or must stop.
---

# Workflow Evaluator

## Set checks before execution

For each node, define:
- expected output and required evidence;
- an observable pass condition;
- correctness, completeness, freshness, and safety checks that apply;
- what failure invalidates downstream work;
- what cannot be checked in the current host.

Do not invent numeric scores when a pass/fail predicate is clearer. Never treat model confidence or a polished response as evidence.

## Evaluate

1. Compare actual output to the node contract and the user's acceptance criteria.
2. Verify material facts against primary sources or independent reads where available.
3. Check tool action outcomes separately from the model's summary of those outcomes.
4. Mark each criterion as pass, fail, or unknown, with evidence.
5. Route a failure to local diagnosis; route an unknown to a targeted check or a transparent limitation.

## Repair and stop

- Retry a node no more than three times by default, correcting the cause between attempts.
- Rerun only downstream nodes invalidated by the repair.
- Do not repeat external or destructive actions until state has been checked for prior success.
- Stop immediately on a permission denial, unsafe side effect, or missing required approval.
- After the retry budget, preserve successful nodes and report the failing criterion and evidence.

## Completion

Call the workflow complete only when every required acceptance criterion passes or the user accepts a clearly described limitation. Report checks performed, evidence, unknowns, and any failed nodes.

