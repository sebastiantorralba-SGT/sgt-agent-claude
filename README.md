# Seguritech Agents — Claude Code plugin

Claude Code plugin that installs the neutral [`agents`](https://git.seguritech.org:92/bigdata-seguritech/code-template) CLI and exposes it through an MCP server so the agent can search, install, validate, and publish capabilities from the team registry.

This repo is the Claude port of [`sgt-agent`](../sgt-agent) (Cursor). Shared logic lives in `mcp-server/`; sync with `scripts/sync-from-sgt-agent.ps1`.

Opt-in: repos stay neutral without this plugin. Skills and rules still live in `.agents/` and `AGENTS.md`; this plugin adds MCP wiring only.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) on PATH
- [Claude Code](https://code.claude.com/) installed and authenticated
- Network access to `git.seguritech.org` for the first CLI install

## Install the plugin

### Team marketplace (recommended)

This repo ships [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) at the root.

1. Push this repository to your Git server.
2. In Claude Code, add the marketplace:

   ```text
   /plugin marketplace add <git-url-to-this-repo>
   ```

3. Install the plugin:

   ```text
   /plugin install agents@sgt-agent-claude
   ```

4. Reload if prompted:

   ```text
   /reload-plugins
   ```

5. Approve the `agents` MCP server on first use (`/plugin` → Errors tab if it fails to start).

### Local development

```bash
claude --plugin-dir .
```

After edits to commands, MCP, hooks, or agents (not skill bodies): `/reload-plugins`.

### CLI bootstrap (manual)

```powershell
.\scripts\ensure-agents.ps1
```

```bash
./scripts/ensure-agents.sh
```

Then sign in (terminal only):

```bash
agents login
```

## Slash commands

Type `/agents:agents-` in the command palette to discover all 24 commands. Each
command tells the agent to prefer the MCP tool and fall back to the CLI when MCP
is unavailable. Shared routing rules live in
[`commands/references/routing.md`](commands/references/routing.md).

**Prerequisite:** before any MCP tool, slash command, or plugin skill, the agent
must read `AGENTS.md` at the repo root where the operation applies (see Step 0
in routing.md). If missing, suggest `/agents:agents-init`.

## Plugin skills

| Skill | When |
| --- | --- |
| `agents-entrypoint` | Before any MCP tool or `/agents:agents-*` command — read `AGENTS.md` first |
| `bootstrap` | Install CLI, verify login, confirm MCP connectivity |

| Slash command | MCP tool | CLI equivalent |
| --- | --- | --- |
| `/agents:agents-version` | `agents_version` | `agents version` |
| `/agents:agents-search` | `agents_search` | `agents search` |
| `/agents:agents-list` | `agents_list` | `agents list` |
| `/agents:agents-info` | `agents_info` | `agents info` |
| `/agents:agents-add` | `agents_add` | `agents add` |
| `/agents:agents-update` | `agents_update` | `agents update` |
| `/agents:agents-areas` | `agents_areas` | `agents areas` |
| `/agents:agents-kinds` | `agents_kinds` | `agents kinds` |
| `/agents:agents-taxonomy` | `agents_taxonomy` | `agents taxonomy` |
| `/agents:agents-init` | `agents_init` | `agents init` |
| `/agents:agents-migrate` | `agents_migrate` | `agents migrate` |
| `/agents:agents-check` | `agents_check` | `agents check` |
| `/agents:agents-link` | `agents_link` | `agents link` |
| `/agents:agents-new` | `agents_new` | `agents new` |
| `/agents:agents-propose` | `agents_propose` | `agents propose` |
| `/agents:agents-publish` | `agents_publish` | `agents publish` |
| `/agents:agents-unpublish` | `agents_unpublish` | `agents unpublish` |
| `/agents:agents-kb-list` | `agents_kb_list` | `agents kb list` |
| `/agents:agents-kb-pull` | `agents_kb_pull` | `agents kb pull` |
| `/agents:agents-kb-push` | `agents_kb_push` | `agents kb push` |
| `/agents:agents-core-list` | `agents_core_list` | `agents core list` |
| `/agents:agents-core-add` | `agents_core_add` | `agents core add` |
| `/agents:agents-core-rm` | `agents_core_rm` | `agents core rm` |
| `/agents:agents-login-status` | `agents_login_status` | (MCP only — credentials file) |

No slash command for `login`, `logout`, or `release` — run those in a terminal.

## MCP tools

Same surface as the Cursor plugin — see [`sgt-agent` README](../sgt-agent/README.md#mcp-tools).

Workspace cwd for repo-local commands defaults to `${CLAUDE_PROJECT_DIR}` via
[`.mcp.json`](.mcp.json). Override with env `AGENTS_BIN` or `AGENTS_GIT_SPEC`.

## Recommended workflow

1. Read `AGENTS.md` at the repo root
2. Bootstrap — skill `bootstrap` or MCP `agents_version`
3. `agents search` → `agents add`
4. `agents kb pull`
5. Work in the repo
6. `agents check` → `agents propose`

## Sync from Cursor plugin

When `sgt-agent` changes shared assets:

```powershell
.\scripts\sync-from-sgt-agent.ps1
```

Then review `skills/` and `commands/references/routing.md` for Claude-specific wording.

## Development

```bash
cd mcp-server
uv sync --group dev
uv run pytest
uv run agents-mcp
```

Validate the plugin manifest:

```bash
claude plugin validate .
```

## Publish checklist

1. Bump `version` in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) and [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).
2. Run `claude plugin validate .` and `uv run pytest` in `mcp-server/`.
3. Push to Git; users refresh the marketplace or reinstall.
4. Optional: submit to Anthropic community marketplace after internal rollout.

## License

MIT — see [LICENSE](LICENSE).
