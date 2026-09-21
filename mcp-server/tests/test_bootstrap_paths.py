"""Binary resolution on Windows-style paths."""

import os
from pathlib import Path

from agents_mcp import bootstrap


def test_local_bin_candidates_include_windows_profile(monkeypatch, tmp_path):
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    candidates = bootstrap.local_bin_candidates()
    assert any("agents.exe" in str(path) for path in candidates)


def test_find_agents_bin_honors_override(monkeypatch, tmp_path):
    binary = tmp_path / "custom-agents.exe"
    binary.write_text("", encoding="utf-8")
    monkeypatch.setenv("AGENTS_BIN", str(binary))
    assert bootstrap.find_agents_bin() == binary


def test_resolve_workspace_prefers_agents_workspace(monkeypatch, tmp_path):
    workspace = tmp_path / "repo"
    workspace.mkdir()
    monkeypatch.setenv("AGENTS_WORKSPACE", str(workspace))
    assert bootstrap.resolve_workspace() == workspace.resolve()


def test_login_status_missing_credentials(tmp_path, monkeypatch):
    creds = tmp_path / "credentials.json"
    monkeypatch.setenv("AGENTS_CREDENTIALS", str(creds))
    status = bootstrap.login_status()
    assert status["logged_in"] is False
    assert "agents login" in status["message"]


def test_login_status_with_token(tmp_path, monkeypatch):
    creds = tmp_path / "credentials.json"
    creds.write_text(
        '{"https://review.example.com": {"token": "abc"}}',
        encoding="utf-8",
    )
    monkeypatch.setenv("AGENTS_CREDENTIALS", str(creds))
    status = bootstrap.login_status()
    assert status["logged_in"] is True
    assert status["services"] == ["https://review.example.com"]
