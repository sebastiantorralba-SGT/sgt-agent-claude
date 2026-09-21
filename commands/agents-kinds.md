---
description: Show project kinds and what each brings
disable-model-invocation: true
---

# agents kinds

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **defaults** (optional): use CLI defaults
- **publish** (optional): publish kinds to registry (admin)

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_kinds` with the arguments above.
2. **Shell fallback** from workspace root: `agents kinds [--defaults] [--publish]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
