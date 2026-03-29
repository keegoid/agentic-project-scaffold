"""Write canonical project metadata for the scaffold."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ops.common import CONFIG_PATH, ensure_directory, write_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Human-friendly project name")
    parser.add_argument("--slug", required=True, help="Short filesystem and repo slug")
    parser.add_argument("--summary", required=True, help="One-line project summary")
    parser.add_argument(
        "--source-of-truth",
        action="append",
        dest="source_of_truth",
        default=[],
        help="Repeatable flag for source-of-truth files or systems",
    )
    parser.add_argument("--artifact-dir", default="artifacts", help="Directory for generated outputs")
    parser.add_argument("--work-item-dir", default="work-items", help="Directory for canonical work items")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_directory(CONFIG_PATH.parent)
    write_json(
        CONFIG_PATH,
        {
            "name": args.name,
            "slug": args.slug,
            "summary": args.summary,
            "source_of_truth": args.source_of_truth,
            "artifact_directory": args.artifact_dir,
            "work_item_directory": args.work_item_dir,
        },
    )
    ensure_directory(CONFIG_PATH.parent.parent / args.artifact_dir)
    ensure_directory(CONFIG_PATH.parent.parent / args.work_item_dir)
    print(f"Wrote {CONFIG_PATH}")


if __name__ == "__main__":
    main()
