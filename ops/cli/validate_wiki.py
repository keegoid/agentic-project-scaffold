"""Validate wiki article metadata and wikilinks."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ops.common import REPO_ROOT


WIKI_ROOT = REPO_ROOT / "docs" / "wiki"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_FIELDS = ("title", "summary", "status", "updated", "tags")
VALID_STATUSES = {"seed", "active", "deprecated"}


@dataclass(frozen=True)
class WikiIssue:
    path: Path
    message: str


def iter_wiki_files(root: Path = WIKI_ROOT) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    frontmatter: dict[str, object] = {}
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        key, separator, value = stripped.partition(":")
        if not separator:
            continue
        frontmatter[key.strip()] = parse_frontmatter_value(value.strip())
    return frontmatter, text[match.end() :]


def parse_frontmatter_value(value: str) -> object:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("'\"") for item in inner.split(",")]
    return value.strip("'\"")


def iter_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append(target)
    return links


def resolve_wikilink(target: str, current_path: Path, root: Path = WIKI_ROOT) -> Path:
    if target.endswith(".md"):
        relative_target = Path(target)
    else:
        relative_target = Path(f"{target}.md")
    if not relative_target.is_absolute():
        relative_target = (current_path.parent / relative_target).resolve().relative_to(root.resolve())
    return root / relative_target


def validate_article(path: Path, root: Path = WIKI_ROOT) -> list[WikiIssue]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    issues: list[WikiIssue] = []
    relative_path = path.relative_to(root)

    if not frontmatter:
        issues.append(WikiIssue(relative_path, "missing YAML frontmatter"))
        return issues

    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            issues.append(WikiIssue(relative_path, f"missing frontmatter field: {field}"))

    status = frontmatter.get("status")
    if status and status not in VALID_STATUSES:
        issues.append(WikiIssue(relative_path, f"invalid status: {status}"))

    updated = frontmatter.get("updated")
    if updated and (not isinstance(updated, str) or not DATE_RE.match(updated)):
        issues.append(WikiIssue(relative_path, "updated must use YYYY-MM-DD"))

    tags = frontmatter.get("tags")
    if tags is not None and not isinstance(tags, list):
        issues.append(WikiIssue(relative_path, "tags must be a YAML list"))

    if not body.lstrip().startswith("# "):
        issues.append(WikiIssue(relative_path, "article body should start with an H1 heading"))

    for target in iter_wikilinks(body):
        resolved = resolve_wikilink(target, path, root=root)
        if not resolved.exists():
            issues.append(WikiIssue(relative_path, f"broken wikilink: [[{target}]]"))

    return issues


def validate_wiki(root: Path = WIKI_ROOT) -> list[WikiIssue]:
    issues: list[WikiIssue] = []
    files = iter_wiki_files(root)

    if not files:
        return [WikiIssue(Path("docs/wiki"), "wiki directory does not contain any markdown files")]

    if not (root / "README.md").exists():
        issues.append(WikiIssue(Path("docs/wiki"), "missing README.md"))

    for path in files:
        issues.extend(validate_article(path, root=root))

    return issues


def main() -> None:
    issues = validate_wiki()
    if issues:
        for issue in issues:
            print(f"{issue.path}: {issue.message}")
        raise SystemExit(1)

    print(f"Validated {len(iter_wiki_files())} wiki article(s).")


if __name__ == "__main__":
    main()
