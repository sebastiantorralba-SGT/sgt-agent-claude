---
description: Show detail for a capability by name
disable-model-invocation: true
---

# agents info

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **name** (required): capability name

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_info` with the arguments above.
2. **Shell fallback** from workspace root: `agents info <name>`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
