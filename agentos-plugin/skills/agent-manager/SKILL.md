---
name: agent-manager
description: Use when a task benefits from assigning work to specialist roles, coordinating native subagents, parallel research, or merging independent results.
---

# Agent Manager

## Determine what can actually run

1. Inspect the current host's live tool list for a native subagent or delegation tool. Use the exact exposed tool and schema.
2. Distinguish a real spawned worker from a role skill, a prompt template, or a model pass. A skill profile alone does not create another process.
3. If delegation is unavailable, run the relevant specialist passes in sequence within the current conversation. Do not describe them as separate agents or as parallel work.

## Delegate with a contract

For every real worker, provide:
- one bounded objective and the relevant context;
- explicit inputs and an expected output format;
- evidence requirements and uncertainty reporting;
- write boundaries and whether tools may be used;
- a stop condition and deadline/attempt limit.

Delegate read-only independent work in parallel when useful. Serialize changes to shared files, external accounts, or other mutable state. Give each worker its own file or clearly bounded area when concurrent edits are required.

## Specialist roster

- Research: authoritative sources, current facts, claim-to-source mapping.
- Engineering: code, system design, debugging, implementation.
- QA and security: acceptance checks, edge cases, threat and permission review.
- Data analysis: provenance, quality, methods, uncertainty, reproducibility.
- Automation: tool schemas, ordered actions, idempotency, independent state checks.
- Product strategy: user outcome, constraints, prioritization, delivery sequence.
- Creative: brief, audience, concept, artifact, factual and rights review.
- Learning evaluation: outcome scoring, repeated failure patterns, reversible proposals.

Select only roles that materially help the requested outcome.

## Merge and close

1. Check that each delegated result answers its assignment and includes evidence.
2. Resolve disagreements by returning to primary evidence or the user's acceptance criteria; do not average incompatible claims.
3. Integrate only supported findings. Preserve unknowns and blockers.
4. Verify the merged result against the overall task criteria.
5. Report the number of workers only when a host tool confirms they were spawned; otherwise describe sequential specialist passes.

## Limits

Never invent an agent identifier, claim background execution, or imply persistent worker memory without host evidence. Agent access inherits the host's available tools and permissions; delegation does not grant more authority.

