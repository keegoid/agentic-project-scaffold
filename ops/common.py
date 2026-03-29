"""Shared helpers for deterministic project operations."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "config" / "project.json"


@dataclass(frozen=True)
class ProjectConfig:
    """Minimal project metadata used by deterministic scripts."""

    name: str
    slug: str
    summary: str
    source_of_truth: list[str]
    artifact_directory: Path
    work_item_directory: Path


def ensure_directory(path: Path) -> Path:
    """Create a directory if needed and return it."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(path: Path) -> dict[str, Any]:
    """Read a JSON file into a dictionary."""
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    """Write a dictionary as canonical JSON."""
    ensure_directory(path.parent)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slugify(value: str) -> str:
    """Convert free-form text into a filesystem-friendly slug."""
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "item"


def utc_timestamp() -> str:
    """Return a timezone-aware UTC timestamp."""
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def load_project_config(path: Path = CONFIG_PATH) -> ProjectConfig:
    """Load project metadata from config/project.json."""
    payload = read_json(path)
    return ProjectConfig(
        name=payload["name"],
        slug=payload["slug"],
        summary=payload["summary"],
        source_of_truth=list(payload.get("source_of_truth", [])),
        artifact_directory=REPO_ROOT / payload.get("artifact_directory", "artifacts"),
        work_item_directory=REPO_ROOT / payload.get("work_item_directory", "work-items"),
    )
