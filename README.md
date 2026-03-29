# Agentic Project Scaffold

A reusable starter for projects where humans and coding agents collaborate.

This scaffold borrows a simple operating model:

- `AGENTS.md` and `CLAUDE.md` tell agents how to work inside the repo
- `playbooks/` define goals, sequencing, and contracts
- `ops/cli/` holds deterministic scripts for repeatable execution
- agents handle reasoning, judgment, review, and ambiguity

Use it when you want a project to be friendly to Codex, Claude Code, or a similar agent without turning the repo into a pile of ad hoc prompts and one-off scripts.

## Why This Structure Works

The scaffold is opinionated about separation of concerns:

- agents decide what should happen
- scripts perform the steps that should happen the same way every time
- playbooks capture workflows that need both

That split keeps the repo easier to audit, easier to automate, and easier to hand off between people and tools.

## Quickstart

1. Create a virtual environment:

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

2. Customize the project metadata:

```bash
./scripts/python ops/cli/init_project.py \
  --name "Your Project" \
  --slug your-project \
  --summary "What this repo is for" \
  --source-of-truth README.md \
  --source-of-truth config/project.json
```

3. Review and adapt:

- `AGENTS.md`
- `CLAUDE.md`
- `playbooks/`
- `config/project.json`

4. Validate the scaffold:

```bash
./scripts/python ops/cli/check_scaffold.py
python -m unittest discover -s tests
```

## Example Workflow

Capture a work item deterministically:

```bash
./scripts/python ops/cli/create_work_item.py \
  --title "Document deployment flow" \
  --description "Write the first deployment playbook for the repo" \
  --outcome "A concrete deployment runbook lives in playbooks/" \
  --owner "agent"
```

Render a markdown handoff:

```bash
./scripts/python ops/cli/render_handoff.py --work-item-id document-deployment-flow
```

These scripts are intentionally small. They are examples of the pattern, not a framework you must keep forever.

## Repository Layout

```text
.
├── AGENTS.md
├── CLAUDE.md
├── config/
├── ops/
│   ├── cli/
│   └── common.py
├── playbooks/
├── scripts/
├── tests/
└── artifacts/
```

## Adapting This Scaffold

- Replace the generic work-item examples with scripts that fit your domain.
- Keep deterministic I/O, syncs, exports, and validations in `ops/cli/`.
- Keep agent expectations in `AGENTS.md` and mirror them in `CLAUDE.md` if you use multiple tools.
- Add or remove playbooks as workflows mature.
- Mark the repository as a GitHub template if you want one-click reuse.

## Open Source Notes

This repo is designed to be published as a public template repository. The included GitHub Actions workflow runs basic validation so forks and derived repos start with a working baseline.
