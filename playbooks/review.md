# Review Playbook

## When To Use It

Use this playbook before handoff, merge, or release.

## Sequence

1. Agent reviews the change for behavior regressions, missing tests, and contract drift.
2. Run `ops/cli/check_scaffold.py` or the relevant project-specific validators.
3. Run `ops/cli/validate_wiki.py` when the wiki changed.
4. Run the test suite for deterministic logic.
5. If needed, run `ops/cli/render_handoff.py` to produce a concise markdown summary.

## Contract

- Findings come before summaries.
- Validation is explicit, not implied.
- Handoffs point to source-of-truth files and any unresolved risks.
