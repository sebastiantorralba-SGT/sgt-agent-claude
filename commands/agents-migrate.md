---
description: Consolidate per-tool config into neutral structure
disable-model-invocation: true
---

# agents migrate

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **apply** (optional): execute plan (default false)
- **clean** (optional): remove originals after migrate
- **area** (optional): target area for migrated skills

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_migrate` with the arguments above.
2. **Shell fallback** from workspace root: `agents migrate [--apply] [--clean] [--area <a>]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
