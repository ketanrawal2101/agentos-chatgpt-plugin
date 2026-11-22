---
name: workflow-engine
description: Use to plan and execute complex tasks as node graphs with dependencies, parallel work, bounded observe-evaluate-repair loops, retries, and acceptance tests.
---

# Workflow Engine: Node Graph, Observe, Evaluate, Repair

## Plan as a graph
Create a task graph with explicit node IDs and edges. Nodes should be small, observable, and independently verifiable. Typical node types: input, research, transform, tool action, approval, validation, merge, and report.

For each node define:
- objective and input contract;
- selected tool/skill and why it fits;
- expected output shape;
- success predicate / acceptance test;
- side-effect and idempotency classification;
- retry budget and recovery route;
- dependency edges.

## Execution loop
Use this controlled loop for each node:
1. **Observe** — collect the actual tool response, output artifact, and error metadata.
2. **Evaluate** — compare the result with the node's success predicate and task acceptance criteria.
3. **Diagnose** — identify the root cause and affected downstream nodes.
4. **Adapt** — revise the smallest necessary input, plan, tool choice, or transformation.
5. **Re-execute** — rerun only safe, invalidated work within the retry budget.
6. **Verify** — independently check the repaired result.

The loop is not “repeat from the beginning until it works.” It is a bounded local repair loop with explicit stop conditions. If a node cannot be repaired safely, stop and report the evidence.

## Parallelism
Parallelize only independent nodes. Do not parallelize writes that can conflict, actions with ordering requirements, or tasks that depend on a shared mutable resource. Merge outputs through a validation node.

## Human gates
Pause at the host's required approval step before consequential side effects. Explain what action is requested and why. A denial or cancellation terminates that action path; continue unrelated permitted nodes.

## Quality gates
Use objective checks: schema validation, unit/integration tests, file existence and readability, source cross-checks, diff review, output completeness, or explicit user acceptance criteria. Do not use confidence language as a substitute for evidence.

## Failure policy
- Transient errors: bounded retry if safe.
- Schema errors: correct the request against the declared schema before retrying.
- Authentication/permission errors: stop and request the supported connection/approval action; do not loop.
- Ambiguous inputs: ask one targeted clarification.
- Incorrect result: revise the responsible node and rerun dependent nodes.
- Irrecoverable failure: preserve completed work and report the blocker.

