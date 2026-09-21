---
description: Retire a capability from the registry (irreversible)
disable-model-invocation: true
---

# agents unpublish

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **name** (required): capability name
- **version** (optional): single version to retire
- **all_versions** (optional): retire all versions

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_unpublish` with the arguments above.
2. **Shell fallback** from workspace root: `agents unpublish <name> [--version V] [--all] --yes`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
