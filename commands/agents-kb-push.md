---
description: Upload changed knowledge files to the registry
disable-model-invocation: true
---

# agents kb push

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **delete** (optional): remove remote files missing locally

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_kb_push` with the arguments above.
2. **Shell fallback** from workspace root: `agents kb push [--delete]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
- On missing `.agents/`, suggest `/agents:agents-init` first.
