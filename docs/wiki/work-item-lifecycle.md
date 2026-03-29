---
title: Work Item Lifecycle
summary: How requests become durable records, implementation work, review, and handoff in the scaffold.
status: active
updated: 2026-03-28
tags: [workflow, work-items]
---

# Work Item Lifecycle

The scaffold expects durable requests to move through a small set of explicit stages:

1. Intake creates or updates a canonical work item.
2. Planning turns the work item into an approach.
3. Implementation combines agent judgment with deterministic scripts.
4. Review checks for regressions, gaps, and contract drift.
5. Release or handoff communicates the verified outcome.

Use the playbooks as the procedural contract and use the wiki to preserve context that would otherwise be rediscovered repeatedly.

## Related

- [[operating-model]]
- [[README]]
