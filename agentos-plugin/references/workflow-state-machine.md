# AgentOS Workflow State Machine

Use this state model for multi-step work. Keep state in the current conversation or in a host-provided authorized store; the plugin itself is not a database.

| State | Meaning | Allowed next states |
|---|---|---|
| `planned` | Graph and acceptance checks are defined | `ready`, `blocked` |
| `ready` | Preconditions and approvals for the node are satisfied | `running`, `blocked` |
| `running` | The action is in progress | `observed`, `failed`, `paused` |
| `observed` | Actual output/result is recorded in task context | `evaluating` |
| `evaluating` | Result is checked against acceptance criteria | `passed`, `repair`, `blocked` |
| `repair` | Root cause is known and local repair is selected | `ready`, `blocked` |
| `passed` | Node's success predicate has evidence | downstream `ready`, workflow `complete` |
| `paused` | Waiting for required host/user approval or external state | `ready`, `blocked` |
| `failed` | Attempt did not meet the node contract | `repair`, `blocked` |
| `blocked` | Safe progress requires missing permission, information, or capability | `ready` only after the condition changes |

## Invariants

- Every node has an ID, objective, inputs, dependencies, tool/role, expected output, success predicate, side-effect class, and retry cap.
- The graph is acyclic; retry loops belong to one node and are bounded to at most three attempts by default.
- A node cannot become `passed` without evidence for its success predicate.
- Repair only the failed node and rerun descendants whose inputs became stale.
- A node with an uncertain external side effect must be checked for prior success before another attempt.
- A denied approval cannot transition back to `ready` unless the user changes the authorization.
- Finish as `complete` only when all required nodes passed or the user accepted a stated limitation.

