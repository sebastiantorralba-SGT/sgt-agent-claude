# Routing rules for `/agents:agents-*` commands

Apply these rules for every command in this folder and for any direct MCP tool call
(`agents_*`) or plugin skill (`bootstrap`, `agents-entrypoint`).

## Step 0 — AGENTS.md

Before the first MCP tool, slash command, or plugin skill in a session — and again
when switching repos — **read `AGENTS.md` at the repo root** where the operation
applies:

1. **`AGENTS_WORKSPACE`** env var from the plugin MCP config (defaults to
   `${CLAUDE_PROJECT_DIR}`).
2. Else the folder that contains `.agents/` for this task.
3. Else the project directory the user is working in.

In multi-repo sessions, use the root of the repo the user is working in, not
another folder (e.g. `@my-repo/AGENTS.md`, not a sibling folder).

Also read `.agents/memory/INDEX.md` when it exists.

- If `AGENTS.md` is missing: do not invent conventions; tell the user and suggest
  `/agents:agents-init` or `agents init`.
- Do not call MCP or shell until `AGENTS.md` has been read.

## Execution order

1. **MCP first** — if the `agents` MCP server is connected, call the tool named in
   the command (e.g. `agents_search`).
2. **Shell fallback** — only when MCP is unavailable or the tool fails to connect:
   - Run from the **project root** (repo with `.agents/` when the command needs it).
   - Use `agents` on PATH, or on Windows `%USERPROFILE%\.local\bin\agents.exe`.
   - Never use `uvx agents` (not on PyPI).

## Bootstrap

If `agents` is missing, run the plugin **bootstrap** skill or
`scripts/ensure-agents.ps1` / `ensure-agents.sh` before retrying.

## Authentication

- **`agents login` and `agents logout` have no slash command** — they are interactive; run in a terminal.
- Before `propose`, `kb push`, or `core add/rm`, check `agents_login_status` or run `agents login` if auth fails.

## Repo requirements

Commands that touch `.agents/` (`add`, `check`, `propose`, `kb *`, `link`, `new`, …) need a repo seeded with `agents init`. If `.agents/` is missing, say so and suggest `/agents:agents-init` or `agents init`.

## Destructive actions — confirm first

Ask the user explicitly before executing:

| Command | When to confirm |
| --- | --- |
| `/agents:agents-init` | Always — creates/overwrites structure |
| `/agents:agents-migrate` | When applying (`--apply` or apply=true) |
| `/agents:agents-publish` | Always — publishes to team registry |
| `/agents:agents-unpublish` | Always — irreversible |
| `/agents:agents-kb-push` | When `--delete` is requested |
| `/agents:agents-update` | When applying updates without `--dry-run` |

For MCP tools, pass `confirm=true` or `yes=true` only after the user agrees.

## Output

- Show stdout (or parsed JSON from MCP) in the reply.
- If exit code ≠ 0, summarize stderr and suggest the next fix (login, init, `agents check`).
- Do not paste secrets from credentials files.
