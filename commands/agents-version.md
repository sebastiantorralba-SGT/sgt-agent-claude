---
description: Show the installed agents CLI version
disable-model-invocation: true
---

# agents version

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- No arguments required.

## Execute

1. **MCP (preferred):** call `agents_version` with the arguments above.
2. **Shell fallback** from workspace root: `agents version`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
