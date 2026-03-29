---
title: Operating Model
summary: How the scaffold splits reasoning, documented workflow contracts, and deterministic execution.
status: active
updated: 2026-03-28
tags: [architecture, scaffold]
---

# Operating Model

The scaffold separates concerns so that:

- agents handle reasoning, prioritization, tradeoffs, review, and ambiguity
- playbooks define goals, sequencing, and contracts
- `ops/cli/` scripts handle repeatable execution

This keeps the repository easier to audit, easier to automate, and easier to adapt to a domain-specific project later.

## Practical Rule

If a step should happen the same way every time, prefer a tested script or validator over remembering the step through prompt wording alone.

## Related

- [[README]]
- [[work-item-lifecycle]]
