# Documentation

This repository has two separate layers: the ChatGPT plugin source under `agentos-plugin/` and repository custom agents under `.github/agents/`.

- [Architecture and package boundaries](architecture.md)
- [Agent profiles and skill mapping](agent-skill-map.md)
- [Host compatibility](host-compatibility.md)
- [Workflow graph and repair loops](workflows-and-loops.md)
- [Hook event reference](../agentos-plugin/references/hook-event-map.md)
- [Plugin state machine](../agentos-plugin/references/workflow-state-machine.md)
- [Contribution and change process](../CONTRIBUTING.md)
- [Repository change log](../CHANGELOG.md)

The `.agent.md` profiles target GitHub Copilot and compatible VS Code agent workflows. They do not change the installed ChatGPT plugin.
