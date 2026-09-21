---
name: agents-entrypoint
description: Use before any agents MCP tool, /agents:agents-* slash command, or bootstrap workflow — read the repo's AGENTS.md first to load project rules, area, and installed capabilities.
---

# Agents entrypoint

Apply this skill before invoking any surface of the Seguritech Agents plugin:
MCP tools (`agents_search`, `agents_add`, …), `/agents:agents-*` slash commands, or
the `bootstrap` skill.

## Resolve the repo root

1. **`AGENTS_WORKSPACE`** env var from the plugin MCP config (defaults to
   `${CLAUDE_PROJECT_DIR}`).
2. Else the folder that contains `.agents/` for this task.
3. Else the project directory the user is working in.

In multi-repo sessions, use the root of the repo the user is working in — not a
sibling folder.

## Read before you act

1. Read **`AGENTS.md`** at that repo root in full.
2. Read **`.agents/memory/INDEX.md`** when it exists.
3. Only then call MCP, run a slash command, or shell out to `agents`.

If `AGENTS.md` is missing, stop and suggest `/agents:agents-init` or `agents init`. Do
not invent project conventions.

Full routing rules: [commands/references/routing.md](../../commands/references/routing.md).
