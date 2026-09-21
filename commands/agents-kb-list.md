---
description: Compare local knowledge with the registry
disable-model-invocation: true
---

# agents kb list

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- No arguments required.

## Execute

1. **MCP (preferred):** call `agents_kb_list` with the arguments above.
2. **Shell fallback** from workspace root: `agents kb list`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
