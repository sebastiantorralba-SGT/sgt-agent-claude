---
description: Submit a capability for area-admin review
disable-model-invocation: true
---

# agents propose

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **target_name** (required): capability name or path

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_propose` with the arguments above.
2. **Shell fallback** from workspace root: `agents propose <name>`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
- On missing `.agents/`, suggest `/agents:agents-init` first.
