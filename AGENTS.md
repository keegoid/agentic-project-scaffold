# Agent Instructions

This project separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution.

## How To Operate

- **Playbooks** (`playbooks/`) define objectives, sequences, and contracts
- **Agents** handle reasoning, prioritization, tradeoffs, naming, review, and exception handling
- **Ops** (`ops/`, `ops/cli/`) handle deterministic execution such as file writes, API calls, exports, validation, and report generation

**Use ops for repeatable execution.** When a tested script exists in `ops/cli/`, use it.

**Use your judgment for everything else.** Ambiguity resolution, plan quality, product decisions, and edge cases belong with the agent.

## Agent PR Flow

In Keegoid-run environments, agent-authored branch, commit, PR, review,
and sync work is routed through `~/keegoid/ops/bin/agent-pr-flow`; see
`~/keegoid/org/playbooks/agent_pr_flow.md`. This routing applies only
to agent-authored PR work. If that operator tree is unavailable, pause
and ask the repo owner for the Keegoid PR-flow equivalent before using
raw git or GitHub commands for agent-authored PR work.

## Project Rules

- Use `./scripts/python` for repo Python commands
- Keep source-of-truth systems explicit in `README.md` and `config/project.json`
- Use `docs/wiki/` for durable repo knowledge that is too detailed for top-level instructions
- Write generated outputs to `artifacts/` unless the project defines a better home
- Prefer deterministic scripts for validation, syncs, exports, file mutation, and formatting
- Prefer playbooks when a workflow needs both agent reasoning and deterministic execution
- Update playbooks when a workflow becomes repeatable enough to document
- Keep examples small and easy to replace with domain-specific ops
- Trim wiki articles so they stay readable and retrieval-friendly
- Run `./scripts/python ops/cli/validate_wiki.py` after substantial wiki edits

## Key Workflows

- `/intake` - gather context, define the task, and create or update a canonical work item
- `/plan` - turn a work item into an implementation or delivery approach
- `/implement` - perform the work, using ops for any repeatable steps
- `/knowledge` - read or update the wiki when durable project knowledge changes
- `/review` - inspect risks, regressions, and gaps before handoff
- `/release` - package or publish outcomes when the project requires it

## Collaboration Notes

- If both `AGENTS.md` and `CLAUDE.md` exist, keep them aligned
- Favor explicit contracts over clever prompts
- Keep the repo understandable to a human who never uses an agent
