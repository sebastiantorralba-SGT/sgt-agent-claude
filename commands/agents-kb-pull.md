---
description: Fetch project knowledge from the registry
disable-model-invocation: true
---

# agents kb pull

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **overwrite** (optional): overwrite differing local files

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_kb_pull` with the arguments above.
2. **Shell fallback** from workspace root: `agents kb pull [--overwrite]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
