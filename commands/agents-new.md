---
description: Create a capability with path and frontmatter
disable-model-invocation: true
---

# agents new

Read [routing.md](references/routing.md) before executing.

## Prerequisite

Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.

## Input

- **kind** (required): skill | rule | command | subagent | memory
- **name** (required): lowercase-with-hyphens
- **description** (optional): when it applies
- **area** (optional): for skills: area/subarea
- **scope** (optional): shared | project

If required input is missing, ask once.

## Execute

1. **MCP (preferred):** call `agents_new` with the arguments above.
2. **Shell fallback** from workspace root: `agents new <kind> <name> -d "..." [--area <a>] [--scope shared|project]`

## Output

- Show stdout or MCP JSON in the reply.
- On auth errors, tell the user to run `agents login` in a terminal.
