# Playbooks

Playbooks are the bridge between open-ended reasoning and deterministic execution.

A good playbook usually includes:

- the trigger for using it
- the sequence of steps
- which steps belong to the agent
- which steps should call scripts under `ops/cli/`
- the contract for success

Keep playbooks specific enough to guide work, but small enough that they stay easy to maintain.
