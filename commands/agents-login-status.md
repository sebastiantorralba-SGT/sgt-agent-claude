---
description: Check whether a review-service token is stored locally
disable-model-invocation: true
---

# agents login status

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- No arguments required.

## Execute

1. **MCP (preferred):** call `agents_login_status` with the arguments above.
2. **Shell fallback:** not applicable — use MCP only.

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
