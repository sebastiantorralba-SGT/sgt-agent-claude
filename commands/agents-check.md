---
description: Validate .agents/ structure
disable-model-invocation: true
---

# agents check

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **strict** (optional): treat warnings as errors

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_check` with the arguments above.
2. **Shell fallback** from workspace root: `agents check [--strict]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
