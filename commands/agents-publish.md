---
description: Publish directly to the team registry (publisher path)
disable-model-invocation: true
---

# agents publish

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **target_name** (required): capability name or path
- **scope** (optional): shared | project

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_publish` with the arguments above.
2. **Shell fallback** from workspace root: `agents publish <name> [--scope shared|project]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
- On missing `.agents/`, suggest `/agents:agents-init` first.
