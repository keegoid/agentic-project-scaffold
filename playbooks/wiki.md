# Wiki Playbook

## When To Use It

Use this playbook when durable project knowledge changes and that knowledge should survive chat history.

## Sequence

1. Agent decides whether the knowledge belongs in `AGENTS.md`, a playbook, or `docs/wiki/`.
2. Use `docs/wiki/` for mid-granularity knowledge such as architecture notes, workflow contracts, and operational gotchas.
3. Prefer updating an existing article over creating a new one when the topic already has a clear home.
4. Keep each article short, link related topics with `[[wikilinks]]`, and record enough context to help a future agent or human re-orient quickly.
5. Run `./scripts/python ops/cli/validate_wiki.py` after edits.

## Contract

- The wiki captures durable knowledge, not transient task chatter.
- Top-level agent instructions stay concise and point into the wiki when deeper context is needed.
- Wiki pages remain easy to prune, audit, and replace with domain-specific docs later.
