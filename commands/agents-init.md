---
description: Seed README, AGENTS.md and .agents/ in this repo
disable-model-invocation: true
---

# agents init

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **profile** (optional): python-uv | node | empty
- **kind** (optional): development | maintenance | ...
- **area** (optional): area/subarea

If required input is missing, ask once.

## Execute

**Confirm with the user first** (see routing.md). For MCP, pass `confirm=true` or `yes=true` only after approval.

1. **MCP (preferred):** call `agents_init` with the arguments above.
2. **Shell fallback** from workspace root: `agents init [--profile <p>] [--kind <k>] [--area <a>]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
