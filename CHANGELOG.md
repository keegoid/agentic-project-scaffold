# Changelog

## 2026-03-28

- Added a lightweight wiki-based knowledge layer under `docs/wiki/` for durable project context that should survive chat history without expanding top-level agent instructions.
- Added a dedicated wiki playbook and updated scaffold guidance so agents know when to use the wiki, when to keep instructions concise, and when to validate documentation changes.
- Added `ops/cli/validate_wiki.py` plus tests to enforce simple wiki conventions such as frontmatter, headings, and valid wiki links.
