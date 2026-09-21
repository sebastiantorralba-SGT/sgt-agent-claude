---
description: Mark a capability as core for an area
disable-model-invocation: true
---

# agents core add

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **path** (required): area or area/subarea
- **name** (required): published capability name

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_core_add` with the arguments above.
2. **Shell fallback** from workspace root: `agents core add <path> <name>`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
- On missing `.agents/`, suggest `/agents:agents-init` first.
