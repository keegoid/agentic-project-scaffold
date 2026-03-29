from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ops.cli.validate_wiki import parse_frontmatter, validate_wiki


class ValidateWikiTest(unittest.TestCase):
    def test_parse_frontmatter_reads_simple_yaml(self) -> None:
        text = """---
title: Example
summary: Short summary
status: active
updated: 2026-03-28
tags: [wiki, example]
---
# Example
"""
        frontmatter, body = parse_frontmatter(text)
        self.assertEqual(frontmatter["title"], "Example")
        self.assertEqual(frontmatter["tags"], ["wiki", "example"])
        self.assertTrue(body.startswith("# Example"))

    def test_validate_wiki_accepts_well_formed_articles(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                """---
title: Wiki Home
summary: Entry point
status: active
updated: 2026-03-28
tags: [wiki]
---
# Wiki Home

See [[topic]].
""",
                encoding="utf-8",
            )
            (root / "topic.md").write_text(
                """---
title: Topic
summary: Detail page
status: active
updated: 2026-03-28
tags: [topic]
---
# Topic
""",
                encoding="utf-8",
            )
            self.assertEqual(validate_wiki(root), [])

    def test_validate_wiki_reports_broken_links_and_missing_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "README.md").write_text(
                """---
title: Wiki Home
status: active
updated: 2026-03-28
tags: [wiki]
---
# Wiki Home

See [[missing-page]].
""",
                encoding="utf-8",
            )
            issues = validate_wiki(root)
            messages = {issue.message for issue in issues}
            self.assertIn("missing frontmatter field: summary", messages)
            self.assertIn("broken wikilink: [[missing-page]]", messages)


if __name__ == "__main__":
    unittest.main()
