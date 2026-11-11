"""Rebuild the Recently learned and Recent releases sections in README.md."""

from __future__ import annotations

import json
import os
import pathlib
import re
import urllib.error
import urllib.parse
import urllib.request

OWNER = "Mohamedrasheq"
TIL_REPO = "til"
PROFILE_REPO = "Mohamedrasheq"
SKIP_NOTES = {"README.md", "TEMPLATE.md", "BACKLOG.md"}
SKIP_RELEASE_REPOS = {TIL_REPO, PROFILE_REPO}
SEASON = {"early": "03", "mid": "06", "late": "10"}
RECENT_COUNT = 5

TIL_START = "<!-- til starts -->"
TIL_END = "<!-- til ends -->"
RELEASES_START = "<!-- releases starts -->"
RELEASES_END = "<!-- releases ends -->"

API = "https://api.github.com"
RAW = f"https://raw.githubusercontent.com/{OWNER}/{TIL_REPO}/main"
BLOB = f"https://github.com/{OWNER}/{TIL_REPO}/blob/main"
USER_AGENT = f"{OWNER}-profile-readme"


def _headers(*, raw: bool = False) -> dict[str, str]:
    headers = {"User-Agent": USER_AGENT}
    if not raw:
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    token = os.environ.get("GITHUB_TOKEN")
    if token and not raw:
        headers["Authorization"] = f"Bearer {token}"
    return headers


_MISSING = object()


def fetch(url: str, *, raw: bool = False, default=_MISSING):
    req = urllib.request.Request(url, headers=_headers(raw=raw))
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            data = res.read()
    except urllib.error.HTTPError as exc:
        if default is not _MISSING and exc.code in {403, 404, 429}:
            return default
        raise
    if raw:
        return data.decode("utf-8")
    return json.loads(data.decode("utf-8"))


def api(path: str, *, default=None):
    if path.startswith("http"):
        url = path
    else:
        url = API + path
    return fetch(url, default=default)


def api_pages(path: str, *, max_pages: int = 5) -> list:
    items: list = []
    sep = "&" if "?" in path else "?"
    for page in range(1, max_pages + 1):
        chunk = api(f"{path}{sep}per_page=100&page={page}", default=[])
        if not isinstance(chunk, list) or not chunk:
            break
        items.extend(chunk)
        if len(chunk) < 100:
            break
    return items


def learned(text: str) -> tuple[str, str]:
    """Return (label, sort key), matching til/build_index.py."""
    m = re.search(r"_Learned:\s*([^_]+)_", text)
    if not m:
        return "", ""
    label = m.group(1).strip()
    d = re.search(r"(\d{4})-(\d{2})(?:-(\d{2}))?", label)
    if d:
        return label, d.group(0)
    y = re.search(r"(\d{4})", label)
    w = re.search(r"(early|mid|late)", label, re.I)
    key = f"{y.group(1)}-{SEASON[w.group(1).lower()] if w else '06'}" if y else ""
    return label, key


def note_paths() -> list[str]:
    tree = api(f"/repos/{OWNER}/{TIL_REPO}/git/trees/main?recursive=1")
    paths = []
    for entry in tree.get("tree") or []:
        if entry.get("type") != "blob":
            continue
        path = entry.get("path") or ""
        if path.count("/") != 1 or not path.endswith(".md"):
            continue
        name = path.split("/")[-1]
        if name in SKIP_NOTES:
            continue
        paths.append(path)
    return paths


def latest_commit_dates(paths: list[str]) -> dict[str, str]:
    """Latest commit date per file. Cheap when a token is set; otherwise
    walk a short window of commits and fall back to path order."""
    dates: dict[str, str] = {}
    remaining = set(paths)
    if not remaining:
        return dates

    token = os.environ.get("GITHUB_TOKEN")
    # With a token, per-file lookups are cheap (one call each, 5000/hour).
    # Without one, only spend a few calls so we do not burn the 60/hour limit.
    if token:
        for path in paths:
            commits = api(
                f"/repos/{OWNER}/{TIL_REPO}/commits?"
                f"sha=main&path={urllib.parse.quote(path)}&per_page=1",
                default=[],
            )
            if commits:
                dates[path] = commits[0]["commit"]["committer"]["date"]
        return dates

    commits = api(
        f"/repos/{OWNER}/{TIL_REPO}/commits?sha=main&per_page=100",
        default=[],
    )
    budget = 8
    for commit in commits:
        if not remaining or budget <= 0:
            break
        detail = api(f"/repos/{OWNER}/{TIL_REPO}/commits/{commit['sha']}", default=None)
        budget -= 1
        if not detail:
            break
        date = (detail.get("commit") or {}).get("committer", {}).get("date") or ""
        for file in detail.get("files") or []:
            path = file.get("filename")
            if path in remaining and date:
                dates[path] = date
                remaining.discard(path)
    return dates


def recent_til_notes() -> list[tuple[str, str]]:
    paths = note_paths()
    commit_dates = latest_commit_dates(paths)
    notes = []
    for path in paths:
        text = fetch(f"{RAW}/{urllib.parse.quote(path)}", raw=True, default="")
        first = next((line for line in text.splitlines() if line.strip()), path)
        title = first.lstrip("# ").strip() or pathlib.PurePosixPath(path).stem
        _label, key = learned(text)
        notes.append((key, commit_dates.get(path, ""), path, title))
    notes.sort(key=lambda n: n[2])
    notes.sort(key=lambda n: n[1], reverse=True)
    notes.sort(key=lambda n: n[0], reverse=True)
    return [(title, path) for _key, _date, path, title in notes[:RECENT_COUNT]]


def render_til(notes: list[tuple[str, str]]) -> str:
    lines = [f"- [{title}]({BLOB}/{path})" for title, path in notes]
    if lines:
        lines.append("")
    lines.append(f"[all notes](https://github.com/{OWNER}/{TIL_REPO})")
    return "\n".join(lines)


def latest_releases() -> list[tuple[str, str, str, str]]:
    repos = api_pages(f"/users/{OWNER}/repos?type=owner&sort=updated")
    found = []
    for repo in repos:
        name = repo.get("name") or ""
        if name in SKIP_RELEASE_REPOS or repo.get("fork"):
            continue
        release = api(f"/repos/{OWNER}/{name}/releases/latest", default=None)
        if not release or not release.get("html_url"):
            continue
        tag = (release.get("tag_name") or "").strip()
        if not tag:
            continue
        version = tag if tag.lower().startswith("v") else f"v{tag}"
        published = (release.get("published_at") or release.get("created_at") or "")[:10]
        found.append((published, name, version, release["html_url"]))
    found.sort(key=lambda r: r[0], reverse=True)
    return found[:RECENT_COUNT]


def render_releases(releases: list[tuple[str, str, str, str]]) -> str:
    if not releases:
        return ""
    lines = ["### 🚀 Recent releases", ""]
    for published, name, version, url in releases:
        suffix = f" - {published}" if published else ""
        lines.append(f"- [{name} {version}]({url}){suffix}")
    return "\n".join(lines)


def replace_block(text: str, start: str, end: str, body: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    inner = f"{body}\n" if body else ""
    replacement = f"{start}\n{inner}{end}"
    new, n = pattern.subn(replacement, text, count=1)
    if n != 1:
        raise SystemExit(f"Could not find markers {start} ... {end} in README.md")
    return new


def main() -> None:
    readme_path = pathlib.Path(__file__).resolve().parent / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    text = replace_block(text, TIL_START, TIL_END, render_til(recent_til_notes()))
    text = replace_block(text, RELEASES_START, RELEASES_END, render_releases(latest_releases()))
    readme_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
