# Workflow Graphs and Repair Loops

For multi-step requests, AgentOS uses a dependency graph so each step has a clear purpose and a verifiable result.

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

## State reference

The detailed states and invariants are in [workflow-state-machine.md](../agentos-plugin/references/workflow-state-machine.md). In brief: plan, check preconditions, execute, observe, evaluate, repair if needed, then mark passed only when evidence meets the check.

The graph and retry loop are instructions; actual state persistence and parallel execution depend on the host.
