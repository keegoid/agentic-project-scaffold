# Intake Playbook

## When To Use It

Use this playbook when a new request, initiative, or bug report arrives and the repo needs a canonical work item.

## Sequence

1. Agent gathers the goal, constraints, owner, and expected outcome.
2. Agent resolves obvious ambiguity before creating permanent state.
3. Run `ops/cli/create_work_item.py` to create a deterministic JSON record.
4. Agent reviews the resulting work item and adds missing context if needed.

## Contract

- Every durable request has a stable ID.
- The work item captures the desired outcome, not just the first implementation idea.
- The deterministic record is easy for both humans and agents to inspect later.
