---
title: Wiki Home
summary: Entry point and conventions for durable project knowledge in the scaffold.
status: active
updated: 2026-03-28
tags: [wiki, scaffold]
---

# Wiki Home

This directory holds durable project knowledge that should outlive chat history but does not belong in top-level agent instructions.

Start with:

- [[operating-model]]
- [[work-item-lifecycle]]

## Conventions

- Keep articles short enough to scan during implementation or review.
- Prefer updating an existing article over creating overlapping pages.
- Use wiki links to connect related concepts.
- Store workflow contracts in `playbooks/` and use the wiki for explanatory context around those workflows.
- Run `./scripts/python ops/cli/validate_wiki.py` after substantial wiki edits.
