---
name: bootstrap
description: Read AGENTS.md first, then resolve or install the agents CLI with uv, verify login for authenticated commands, and confirm MCP connectivity. Use when the user asks to set up agents, install the CLI, connect this repo to the capability registry, or before search/add/propose/kb workflows when agents is missing or unauthenticated.
---

# Bootstrap agents for Claude Code

## Overview

This plugin ships an MCP server that wraps the neutral `agents` CLI. The CLI is
not on PyPI — install it from the internal git repo with `uv tool install`.

## Rules

- **Read `AGENTS.md`** at the repo root before any MCP tool or `/agents:agents-*` command.
  See the `agents-entrypoint` skill and [routing.md](../../commands/references/routing.md).
- Use `uv tool install`, never `uvx agents` (PyPI name is unclaimed).
- Never call `python -m agents`; the tool lives in its own uv environment.
- On Windows, if `agents` is missing from PATH after install, call
  `%USERPROFILE%\.local\bin\agents.exe` explicitly.
- `agents login` is interactive — run it in a terminal, not via MCP.
- Prefer MCP tools (`agents_search`, `agents_add`, …) over shelling out when
  the MCP server is connected.
- Slash commands are available under `/agents:agents-*` (e.g. `/agents:agents-search`,
  `/agents:agents-list`, `/agents:agents-check`) when this plugin is enabled.

## Process

### 0. Read AGENTS.md

Read `AGENTS.md` at the repo root (and `.agents/memory/INDEX.md` if present) before
installing, searching, or calling MCP. If missing, suggest `/agents:agents-init`.

### 1. Check uv

```bash
uv --version
```

If missing, install from https://docs.astral.sh/uv/

### 2. Check agents

```bash
command -v agents && agents version
```

Windows PowerShell:

```powershell
Get-Command agents -ErrorAction SilentlyContinue; agents version
```

Or run the bundled script:

- Unix: `./scripts/ensure-agents.sh`
- Windows: `./scripts/ensure-agents.ps1`

### 3. Install if missing

```bash
uv tool install "agents @ git+https://git.seguritech.org:92/bigdata-seguritech/code-template.git"
agents login
```

Optional extras:

```bash
uv tool install "agents[gcs,semantic] @ git+https://git.seguritech.org:92/bigdata-seguritech/code-template.git"
```

### 4. Verify MCP

Use the `agents_version` MCP tool. If it fails, check that `uv` is on PATH and
that the plugin MCP server started (Claude Code → `/plugin` → Errors tab).

Use `agents_login_status` before `agents_propose`, `agents_kb_push`, or
`agents_core_add`.

### 5. Typical repo workflow

1. `agents search "what you need"` → `agents add <name>`
2. `agents kb pull`
3. Work in the repo
4. `agents check`
5. `agents propose <name>` (after `agents login` in a terminal)
