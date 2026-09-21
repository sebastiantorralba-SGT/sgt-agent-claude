"""Resolve or install the agents CLI binary."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

DEFAULT_GIT_SPEC = (
    "agents @ git+https://git.seguritech.org:92/bigdata-seguritech/code-template.git"
)
INSTALL_TIMEOUT_SECONDS = 300


def git_spec() -> str:
    return os.environ.get("AGENTS_GIT_SPEC", DEFAULT_GIT_SPEC).strip() or DEFAULT_GIT_SPEC


def local_bin_candidates() -> list[Path]:
    home = Path.home()
    candidates = [
        home / ".local" / "bin" / "agents",
        home / ".local" / "bin" / "agents.exe",
    ]
    if os.name == "nt":
        profile = os.environ.get("USERPROFILE")
        if profile:
            candidates.insert(0, Path(profile) / ".local" / "bin" / "agents.exe")
    return candidates


def find_agents_bin() -> Path | None:
    override = os.environ.get("AGENTS_BIN", "").strip()
    if override:
        path = Path(override)
        if path.is_file():
            return path

    which = shutil.which("agents")
    if which:
        return Path(which)

    for candidate in local_bin_candidates():
        if candidate.is_file():
            return candidate

    return None


def uv_tool_bin_dir() -> Path | None:
    try:
        completed = subprocess.run(
            ["uv", "tool", "dir"],
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if completed.returncode != 0:
        return None
    root = completed.stdout.strip()
    if not root:
        return None
    for name in ("agents.exe", "agents"):
        candidate = Path(root) / name
        if candidate.is_file():
            return candidate
    return None


def install_agents() -> Path:
    if shutil.which("uv") is None:
        raise RuntimeError(
            "uv is not on PATH. Install it from https://docs.astral.sh/uv/ "
            "before using the agents MCP server."
        )

    completed = subprocess.run(
        ["uv", "tool", "install", git_spec()],
        capture_output=True,
        text=True,
        check=False,
        timeout=INSTALL_TIMEOUT_SECONDS,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()
        raise RuntimeError(f"uv tool install failed: {detail}")

    found = find_agents_bin() or uv_tool_bin_dir()
    if found is None:
        raise RuntimeError(
            "agents was installed but the binary could not be found. "
            "Set AGENTS_BIN to its full path."
        )
    return found


def resolve_agents_bin(*, install: bool = True) -> Path:
    found = find_agents_bin()
    if found is not None:
        return found
    if not install:
        raise RuntimeError(
            "agents CLI not found. Run scripts/ensure-agents or set AGENTS_BIN."
        )
    return install_agents()


def resolve_workspace() -> Path:
    for key in ("AGENTS_WORKSPACE", "CURSOR_WORKSPACE", "WORKSPACE_FOLDER"):
        value = os.environ.get(key, "").strip()
        if value:
            path = Path(value)
            if path.is_dir():
                return path.resolve()
    return Path.cwd().resolve()


def credentials_path() -> Path:
    override = os.environ.get("AGENTS_CREDENTIALS", "").strip()
    if override:
        return Path(override)
    return Path.home() / ".config" / "agents" / "credentials.json"


def login_status() -> dict[str, object]:
    creds = credentials_path()
    if not creds.is_file():
        return {
            "logged_in": False,
            "credentials_file": str(creds),
            "message": "No credentials file. Run `agents login` in a terminal.",
        }
    try:
        import json

        data = json.loads(creds.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {
            "logged_in": False,
            "credentials_file": str(creds),
            "message": f"Could not read credentials: {exc}",
        }
    if not data:
        return {
            "logged_in": False,
            "credentials_file": str(creds),
            "message": "Credentials file is empty. Run `agents login`.",
        }
    services = sorted(data.keys())
    return {
        "logged_in": True,
        "credentials_file": str(creds),
        "services": services,
        "message": f"Token stored for {len(services)} review service(s).",
    }
