# Agent Instructions

This project separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution.

## How To Operate

- **Playbooks** (`playbooks/`) define objectives, sequences, and contracts
- **Agents** handle reasoning, prioritization, tradeoffs, naming, review, and exception handling
- **Ops** (`ops/`, `ops/cli/`) handle deterministic execution such as file writes, API calls, exports, validation, and report generation

**Use ops for repeatable execution.** When a tested script exists in `ops/cli/`, use it.

**Use your judgment for everything else.** Ambiguity resolution, plan quality, product decisions, and edge cases belong with the agent.

## Project Rules

- Use `./scripts/python` for repo Python commands
- Keep source-of-truth systems explicit in `README.md` and `config/project.json`
- Write generated outputs to `artifacts/` unless the project defines a better home
- Prefer deterministic scripts for validation, syncs, exports, file mutation, and formatting
- Prefer playbooks when a workflow needs both agent reasoning and deterministic execution
- Update playbooks when a workflow becomes repeatable enough to document
- Keep examples small and easy to replace with domain-specific ops

## Key Workflows

- `/intake` - gather context, define the task, and create or update a canonical work item
- `/plan` - turn a work item into an implementation or delivery approach
- `/implement` - perform the work, using ops for any repeatable steps
- `/review` - inspect risks, regressions, and gaps before handoff
- `/release` - package or publish outcomes when the project requires it

## Collaboration Notes

- If both `AGENTS.md` and `CLAUDE.md` exist, keep them aligned
- Favor explicit contracts over clever prompts
- Keep the repo understandable to a human who never uses an agent
