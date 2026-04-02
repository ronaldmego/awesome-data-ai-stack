#!/usr/bin/env python3
"""
update_stars.py — Inject GitHub star counts into README.md

Usage:
    python3 scripts/update_stars.py [--token YOUR_GITHUB_TOKEN]

Without a token: 60 req/hour (unauthenticated)
With a token:   5000 req/hour

Star counts are appended inline after the repo description:
  [owner/repo](url) - Description ⭐ 12.4k
"""

import re
import sys
import time
import argparse
import urllib.request
import urllib.error
import json


def fmt_stars(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


def get_stars(owner: str, repo: str, token: str | None) -> int | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data.get("stargazers_count")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  ⚠️  Not found: {owner}/{repo}", file=sys.stderr)
        elif e.code == 403:
            print(f"  ⚠️  Rate limited. Add --token.", file=sys.stderr)
        else:
            print(f"  ⚠️  HTTP {e.code} for {owner}/{repo}", file=sys.stderr)
    except Exception as e:
        print(f"  ⚠️  Error for {owner}/{repo}: {e}", file=sys.stderr)
    return None


# Matches: [owner/repo](https://github.com/owner/repo)
REPO_LINK_RE = re.compile(
    r'(\[([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)\]\(https://github\.com/([a-zA-Z0-9_.-]+)/([a-zA-Z0-9_.-]+)\))(.*?)(?:\s*⭐\s*[\d.]+[kKmM]?)?$',
    re.MULTILINE
)


def process_readme(path: str, token: str | None):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    updated_lines = []
    seen = set()
    total = 0
    updated = 0

    for line in lines:
        # Only process list item lines with a GitHub link
        if not line.strip().startswith("- ["):
            updated_lines.append(line)
            continue

        m = REPO_LINK_RE.search(line)
        if not m:
            updated_lines.append(line)
            continue

        owner = m.group(3)
        repo = m.group(4)
        key = f"{owner}/{repo}".lower()

        # Strip existing star badge from line
        line_clean = re.sub(r'\s*⭐\s*[\d.]+[kKmM]?', '', line).rstrip()

        if key in seen:
            updated_lines.append(line_clean)
            continue
        seen.add(key)

        total += 1
        stars = get_stars(owner, repo, token)
        if stars is not None:
            line_clean = f"{line_clean} ⭐ {fmt_stars(stars)}"
            updated += 1
            print(f"  ✅ {owner}/{repo}: {fmt_stars(stars)}")
        else:
            print(f"  ❌ {owner}/{repo}: skipped")

        updated_lines.append(line_clean)
        time.sleep(0.1)  # gentle rate limiting

    new_content = "\n".join(updated_lines)
    # Preserve trailing newline
    if content.endswith("\n"):
        new_content += "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\n✅ Done: {updated}/{total} repos updated in {path}")


def main():
    parser = argparse.ArgumentParser(description="Inject GitHub star counts into README.md")
    parser.add_argument("--token", help="GitHub personal access token (increases rate limit to 5000/hr)")
    parser.add_argument("--readme", default="README.md", help="Path to README.md (default: README.md)")
    args = parser.parse_args()

    token = args.token
    if not token:
        import os
        token = os.environ.get("GITHUB_TOKEN")

    print(f"🌟 Updating star counts in {args.readme}...")
    if token:
        print("  Using authenticated requests (5000 req/hr)")
    else:
        print("  Using unauthenticated requests (60 req/hr) — set GITHUB_TOKEN for more")

    process_readme(args.readme, token)


if __name__ == "__main__":
    main()
