---
description: Update capabilities and/or the CLI (dry-run by default)
disable-model-invocation: true
---

# agents update

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **dry_run** (optional): default true; set false to apply
- **cli_only** (optional): only update CLI
- **force** (optional): replace locally edited capabilities

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_update` with the arguments above.
2. **Shell fallback** from workspace root: `agents update [--dry-run] [--cli] [--force]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
