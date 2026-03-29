"""Validate that the starter repo still has its expected structure."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ops.common import REPO_ROOT, load_project_config


REQUIRED_PATHS = [
    Path("README.md"),
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("scripts/python"),
    Path("config/project.json"),
    Path("playbooks"),
    Path("ops/cli"),
]


def main() -> None:
    config = load_project_config()
    missing = [path for path in REQUIRED_PATHS if not (REPO_ROOT / path).exists()]

    print(f"Project: {config.name}")
    print(f"Slug: {config.slug}")
    print(f"Artifacts: {config.artifact_directory.relative_to(REPO_ROOT)}")
    print(f"Work items: {config.work_item_directory.relative_to(REPO_ROOT)}")

    if missing:
        for path in missing:
            print(f"MISSING {path}")
        raise SystemExit(1)

    print("Scaffold structure looks good.")


if __name__ == "__main__":
    main()
