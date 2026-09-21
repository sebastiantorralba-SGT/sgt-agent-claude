---
description: Install a capability from the registry into .agents/
disable-model-invocation: true
---

# agents add

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **name** (required): capability name
- **version** (optional): specific version

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_add` with the arguments above.
2. **Shell fallback** from workspace root: `agents add <name> [--version <version>]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
