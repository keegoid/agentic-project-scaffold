# Release Playbook

## When To Use It

Use this playbook when the project needs a publishable outcome such as a release note, artifact bundle, or repository publication step.

## Sequence

1. Agent confirms the intended scope.
2. Agent ensures validation has completed.
3. Deterministic packaging or rendering steps go through scripts under `ops/cli/`.
4. Agent writes the final narrative: what changed, why it matters, and what remains.

## Contract

- Release outputs are reproducible where possible.
- Human-facing summaries stay concise and tied to verified work.
- Publishing steps are explicit and auditable.
