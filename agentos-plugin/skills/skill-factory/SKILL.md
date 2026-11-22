---
name: skill-factory
description: Use when creating, revising, splitting, documenting, or validating reusable skills and specialist-agent role definitions for the AgentOS ecosystem.
---

# Skill Factory

## Design principles
Create task-focused skills with clear activation descriptions, explicit inputs, reliable procedures, safety boundaries, and measurable outputs. Prefer small composable skills over one giant prompt. Avoid vague role labels without executable procedures.

## Skill creation workflow
1. Define the user problem, trigger conditions, non-goals, inputs, outputs, tools, and failure modes.
2. Inspect current official documentation and runtime schemas for any APIs or platform-specific features involved.
3. Draft a skill with valid YAML frontmatter (`name`, `description`) and concise procedural sections.
4. Add references only for details that need progressive disclosure; keep paths relative and package-contained.
5. Include examples and acceptance tests where they materially improve reliability.
6. Validate YAML, file paths, tool names, schema assumptions, safety boundaries, and trigger specificity.
7. Run representative positive, negative, ambiguous, and failure-path tests where a test runtime exists.
8. Version the change, retain a changelog, and compare against prior behavior before promotion.

## Agent roles
A specialist agent definition should state: mission, scope, allowed tools, prohibited actions, input/output contract, handoff format, verification criteria, and escalation conditions. Use an actual runtime-specific agent definition only when that runtime supports it. Otherwise label the role as a skill/persona, not a deployed autonomous agent.

## No magic prompt claims
Natural-language instructions are one layer of control, not the whole architecture. Prefer typed tool schemas, structured state, explicit graph edges, deterministic validators, executable tests, and runtime-enforced permissions wherever available. Do not claim that a skill alone installs hooks, creates parallel agents, persists state, or changes ChatGPT's global router.

