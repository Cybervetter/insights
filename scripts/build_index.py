#!/usr/bin/env python3
"""Regenerates the article listing in README.md from articles/*.md
frontmatter. Run by .github/workflows/publish.yml on every push that
touches articles/ -- keeps the repo's own front page in sync with what is
actually published, the same way the site's own /insights hub always
reflects the current article set.
"""
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
README = ROOT / "README.md"
START = "<!-- ARTICLES:START -->"
END = "<!-- ARTICLES:END -->"


def read_frontmatter_field(text: str, field: str) -> str:
    match = re.search(rf'^{field}:\s*"([^"]*)"', text, re.MULTILINE)
    if not match:
        raise ValueError(f"missing frontmatter field: {field}")
    return match.group(1)


def format_date(iso: str) -> str:
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%-d %B %Y")


def build_index() -> str:
    entries = []
    for path in sorted(ARTICLES_DIR.glob("*.md")):
        text = path.read_text()
        title = read_frontmatter_field(text, "title")
        published = read_frontmatter_field(text, "published")
        standfirst = read_frontmatter_field(text, "standfirst")
        entries.append((published, title, standfirst, path.name))

    entries.sort(key=lambda e: e[0], reverse=True)

    lines = []
    for published, title, standfirst, filename in entries:
        lines.append(f"- **[{title}](articles/{filename})** — {format_date(published)}")
        lines.append(f"  {standfirst}")
    return "\n".join(lines)


def main() -> None:
    readme = README.read_text()
    if START not in readme or END not in readme:
        print(f"README.md is missing {START}/{END} markers", file=sys.stderr)
        sys.exit(1)

    index = build_index()
    pattern = re.compile(re.escape(START) + r".*" + re.escape(END), re.DOTALL)
    updated = pattern.sub(f"{START}\n{index}\n{END}", readme)

    if updated != readme:
        README.write_text(updated)
        print("README.md article index updated.")
    else:
        print("README.md article index already up to date.")


if __name__ == "__main__":
    main()
