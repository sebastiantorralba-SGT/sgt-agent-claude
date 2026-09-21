---
description: Search capabilities in this repo and the shared registry
disable-model-invocation: true
---

# agents search

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **query** (required): what you are about to do, in your words
- **area** (optional): filter e.g. arquitectura or bigdata/ml
- **limit** (optional): max results (default 10)

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_search` with the arguments above.
2. **Shell fallback** from workspace root: `agents search "<query>" [--area <area>] [--limit N]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
