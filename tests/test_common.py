from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ops.common import read_json, slugify, write_json


class CommonHelpersTest(unittest.TestCase):
    def test_slugify_normalizes_text(self) -> None:
        self.assertEqual(slugify(" Document deployment flow "), "document-deployment-flow")

    def test_slugify_falls_back_for_empty_input(self) -> None:
        self.assertEqual(slugify("!!!"), "item")

    def test_write_json_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "example.json"
            payload = {"name": "example", "count": 1}
            write_json(path, payload)
            self.assertEqual(read_json(path), payload)


if __name__ == "__main__":
    unittest.main()
