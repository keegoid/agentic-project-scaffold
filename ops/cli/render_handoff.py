"""Render a markdown handoff summary from a stored work item."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ops.common import ensure_directory, load_project_config, read_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-item-id", required=True, help="Work item slug without the .json suffix")
    parser.add_argument("--stdout", action="store_true", help="Print instead of writing a file")
    return parser.parse_args()


def render_markdown(project_name: str, summary: str, work_item: dict) -> str:
    tags = ", ".join(work_item.get("tags", [])) or "none"
    return "\n".join(
        [
            f"# {work_item['title']}",
            "",
            f"Project: {project_name}",
            f"Summary: {summary}",
            f"Status: {work_item['status']}",
            f"Owner: {work_item['owner']}",
            f"Tags: {tags}",
            "",
            "## Request",
            "",
            work_item["description"],
            "",
            "## Desired Outcome",
            "",
            work_item["outcome"],
            "",
            "## Source Of Truth",
            "",
            "- config/project.json",
            "- work-items/" + f"{work_item['id']}.json",
            "",
        ]
    )


def main() -> None:
    args = parse_args()
    config = load_project_config()
    work_item_path = config.work_item_directory / f"{args.work_item_id}.json"
    work_item = read_json(work_item_path)
    markdown = render_markdown(config.name, config.summary, work_item)

    if args.stdout:
        print(markdown)
        return

    handoff_dir = ensure_directory(config.artifact_directory / "hand-offs")
    handoff_path = handoff_dir / f"{args.work_item_id}.md"
    handoff_path.write_text(markdown + "\n", encoding="utf-8")
    print(f"Wrote {handoff_path}")


if __name__ == "__main__":
    main()
