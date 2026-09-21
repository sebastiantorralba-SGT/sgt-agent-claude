---
description: Wire CLAUDE.md import, slash commands, and mcp.json copies
disable-model-invocation: true
---

# agents link

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **central** (optional): link CLAUDE.md stub (default true)
- **commands** (optional): symlink commands (default true)
- **mcp** (optional): copy mcp.json (default true)

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_link` with the arguments above.
2. **Shell fallback** from workspace root: `agents link [--no-central] [--no-commands] [--no-mcp]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
