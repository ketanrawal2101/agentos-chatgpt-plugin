# Agent Profiles and Skill Map

The repository contains nine custom agent profiles in `.github/agents/`. Each uses the `.agent.md` format and maps to the closest reusable AgentOS skill workflow.

| Custom agent profile | Plugin skill support | Scope |
|---|---|---|
| `orchestrator.agent.md` | `agentos-orchestrator`, `agent-manager`, `capability-discovery`, `tool-router`, `workflow-engine` | Intake, planning, coordination, and verification |
| `researcher.agent.md` | `research-agent` | Evidence-led research and citations |
| `engineer.agent.md` | `engineering-agent` | Software implementation and debugging |
| `reviewer.agent.md` | `qa-security-agent`, `workflow-evaluator` | Independent quality and security review |
| `data-analyst.agent.md` | `data-analyst-agent` | Data quality, metrics, and interpretation |
| `product-strategist.agent.md` | `product-strategy-agent` | Requirements, prioritization, and acceptance criteria |
| `automation.agent.md` | `automation-agent`, `approval-governance` | Connected-app and API workflows |
| `creative.agent.md` | `creative-agent` | Creative direction and production briefs |
| `agent-evaluator.agent.md` | `learning-evaluator-agent`, `learning-governance` | Output evaluation and evidence-backed improvement proposals |

Other skills are cross-cutting capabilities rather than separate worker profiles:

- `agentos-greeting` handles greeting-only messages.
- `agentos-versioning`, `skill-factory`, and `learning-governance` govern changes to reusable instructions.
- `approval-governance` and `lifecycle-hooks` define shared safety and runtime boundaries.
- `workflow-evaluator`, `capability-discovery`, and `tool-router` support more than one role.

The profiles do not automatically preload or run their mapped ChatGPT skills. Their host discovers and invokes them according to its own configuration. See [host compatibility](host-compatibility.md).
