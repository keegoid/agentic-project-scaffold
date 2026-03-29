# Implementation Playbook

## When To Use It

Use this playbook when a work item is ready to move from intent into execution.

## Sequence

1. Agent reads the relevant work item and clarifies scope.
2. Agent decides what should be automated versus handled interactively.
3. Deterministic steps go into `ops/cli/` when they are likely to recur.
4. Agent performs the reasoning-heavy parts: architecture, tradeoffs, naming, and exception handling.
5. Agent updates docs or playbooks when a new workflow becomes stable.

## Contract

- Repeated execution should not depend on memory or prompt phrasing alone.
- Deterministic scripts should be small, composable, and easy to test.
- The repo should become easier to operate after each meaningful workflow lands.
