"""Create a deterministic JSON work item for the repo."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ops.common import load_project_config, slugify, utc_timestamp, write_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Short title for the work item")
    parser.add_argument("--description", required=True, help="What needs to happen")
    parser.add_argument("--outcome", required=True, help="Definition of done")
    parser.add_argument("--owner", default="agent", help="Who currently owns the work item")
    parser.add_argument("--status", default="new", help="Current work item status")
    parser.add_argument("--tag", action="append", default=[], help="Optional repeatable tag")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_project_config()
    work_item_id = slugify(args.title)
    work_item_path = config.work_item_directory / f"{work_item_id}.json"
    payload = {
        "created_at": utc_timestamp(),
        "description": args.description,
        "id": work_item_id,
        "outcome": args.outcome,
        "owner": args.owner,
        "status": args.status,
        "tags": args.tag,
        "title": args.title,
    }
    write_json(work_item_path, payload)
    print(f"Wrote {work_item_path}")


if __name__ == "__main__":
    main()
