---
description: List installed capabilities or the full registry
disable-model-invocation: true
---

# agents list

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **area** (optional): filter by area
- **registry** (optional): set true to list --registry

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_list` with the arguments above.
2. **Shell fallback** from workspace root: `agents list [--area <area>] [--registry]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
