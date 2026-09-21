"""Stdio MCP server exposing the agents CLI as typed tools."""

from __future__ import annotations

from typing import Literal

from mcp.server.mcpserver import MCPServer

from .bootstrap import login_status, resolve_agents_bin
from .runner import AgentsRunner, require_confirmation

mcp = MCPServer("agents")
_runner: AgentsRunner | None = None


def runner() -> AgentsRunner:
    global _runner
    if _runner is None:
        resolve_agents_bin()
        _runner = AgentsRunner()
    return _runner


def _call(args: list[str]) -> str:
    result = runner().run(args)
    return runner().format(result)


# --- Meta ---


@mcp.tool()
def agents_version() -> str:
    """Show the installed agents CLI version."""
    return _call(["version"])


@mcp.tool()
def agents_login_status() -> str:
    """Check whether a review-service token is stored locally (agents login)."""
    import json

    return json.dumps(login_status(), indent=2)


# --- Discover ---


@mcp.tool()
def agents_search(
    query: str,
    area: str | None = None,
    limit: int = 10,
    local_only: bool = False,
    all_scopes: bool = False,
    refresh: bool = False,
) -> str:
    """Search capabilities in this repo and the shared registry."""
    args = ["search", query, "--limit", str(limit)]
    if area:
        args.extend(["--area", area])
    if local_only:
        args.append("--local")
    if all_scopes:
        args.append("--all-scopes")
    if refresh:
        args.append("--refresh")
    return _call(args)


@mcp.tool()
def agents_list(
    area: str | None = None,
    registry: bool = False,
    all_scopes: bool = False,
) -> str:
    """List installed capabilities or everything in the registry."""
    args = ["list"]
    if area:
        args.extend(["--area", area])
    if registry:
        args.append("--registry")
    if all_scopes:
        args.append("--all-scopes")
    return _call(args)


@mcp.tool()
def agents_info(name: str) -> str:
    """Detail of a capability, local or from the registry."""
    return _call(["info", name])


@mcp.tool()
def agents_areas() -> str:
    """Show the area tree from the registry."""
    return _call(["areas"])


@mcp.tool()
def agents_kinds(defaults: bool = False, publish: bool = False) -> str:
    """Show project kinds and what each one brings."""
    args = ["kinds"]
    if defaults:
        args.append("--defaults")
    if publish:
        args.append("--publish")
    return _call(args)


@mcp.tool()
def agents_taxonomy(defaults: bool = False, publish: bool = False) -> str:
    """Show the taxonomy or publish it to the team registry."""
    args = ["taxonomy"]
    if defaults:
        args.append("--defaults")
    if publish:
        args.append("--publish")
    return _call(args)


# --- Install ---


@mcp.tool()
def agents_add(name: str, version: str | None = None) -> str:
    """Install a capability from the registry into .agents/."""
    args = ["add", name]
    if version:
        args.extend(["--version", version])
    return _call(args)


@mcp.tool()
def agents_update(
    dry_run: bool = True,
    cli_only: bool = False,
    capabilities_only: bool = False,
    force: bool = False,
) -> str:
    """Update capabilities in this repo and/or the CLI itself."""
    args = ["update"]
    if dry_run:
        args.append("--dry-run")
    if cli_only:
        args.append("--cli")
    if capabilities_only:
        args.append("--capabilities")
    if force:
        args.append("--force")
    return _call(args)


# --- Repo ---


@mcp.tool()
def agents_init(
    profile: str = "python-uv",
    kind: str | None = None,
    area: str | None = None,
    force: bool = False,
    no_fetch: bool = False,
    bucket: str | None = None,
    confirm: bool = False,
) -> str:
    """Seed README, AGENTS.md and .agents/ in this repo."""
    require_confirmation(confirmed=confirm, action="agents_init")
    args = ["init", "--profile", profile]
    if kind:
        args.extend(["--kind", kind])
    if area:
        args.extend(["--area", area])
    if force:
        args.append("--force")
    if no_fetch:
        args.append("--no-fetch")
    if bucket:
        args.extend(["--bucket", bucket])
    return _call(args)


@mcp.tool()
def agents_migrate(
    apply: bool = False,
    clean: bool = False,
    layout: bool = False,
    area: str | None = None,
    kind: str | None = None,
    profile: str | None = None,
    from_central: str | None = None,
    all_project: bool = False,
    bucket: str | None = None,
    confirm: bool = False,
) -> str:
    """Consolidate a repo with per-tool config into the neutral structure."""
    if apply or clean:
        require_confirmation(confirmed=confirm, action="agents_migrate")
    args = ["migrate"]
    if apply:
        args.append("--apply")
    if clean:
        args.append("--clean")
    if layout:
        args.append("--layout")
    if area:
        args.extend(["--area", area])
    if kind:
        args.extend(["--kind", kind])
    if profile:
        args.extend(["--profile", profile])
    if from_central:
        args.extend(["--from", from_central])
    if all_project:
        args.append("--all-project")
    if bucket:
        args.extend(["--bucket", bucket])
    return _call(args)


@mcp.tool()
def agents_check(strict: bool = False) -> str:
    """Validate .agents/ structure. Exit code non-zero if errors exist."""
    args = ["check"]
    if strict:
        args.append("--strict")
    return _call(args)


@mcp.tool()
def agents_link(
    central: bool = True,
    commands: bool = True,
    mcp: bool = True,
) -> str:
    """Wire up CLAUDE.md import, slash commands, and mcp.json copies (opt-in)."""
    args = ["link"]
    if not central:
        args.append("--no-central")
    if not commands:
        args.append("--no-commands")
    if not mcp:
        args.append("--no-mcp")
    return _call(args)


# --- Authoring ---


@mcp.tool()
def agents_new(
    kind: Literal["skill", "rule", "command", "subagent", "memory"],
    name: str,
    description: str | None = None,
    area: str | None = None,
    scope: Literal["shared", "project"] = "shared",
    tags: str | None = None,
) -> str:
    """Create a capability with the right path and frontmatter."""
    args = ["new", kind, name, "--scope", scope]
    if description:
        args.extend(["--description", description])
    if area:
        args.extend(["--area", area])
    if tags:
        args.extend(["--tags", tags])
    return _call(args)


# --- Publish ---


@mcp.tool()
def agents_propose(target_name: str) -> str:
    """Submit a capability for area-admin review instead of publishing directly."""
    return _call(["propose", target_name])


@mcp.tool()
def agents_publish(
    target_name: str,
    scope: Literal["shared", "project"] | None = None,
    no_vector: bool = False,
    confirm: bool = False,
) -> str:
    """Publish a capability directly to the team registry (publisher path)."""
    require_confirmation(confirmed=confirm, action="agents_publish")
    args = ["publish", target_name]
    if scope:
        args.extend(["--scope", scope])
    if no_vector:
        args.append("--no-vector")
    return _call(args)


@mcp.tool()
def agents_unpublish(
    name: str,
    version: str | None = None,
    all_versions: bool = False,
    yes: bool = False,
) -> str:
    """Retire a capability from the shared registry (irreversible)."""
    require_confirmation(confirmed=yes, action="agents_unpublish")
    args = ["unpublish", name]
    if version:
        args.extend(["--version", version])
    if all_versions:
        args.append("--all")
    args.append("--yes")
    return _call(args)


# --- Knowledge ---


@mcp.tool()
def agents_kb_list() -> str:
    """Compare local .agents/knowledge/ with the registry for this project."""
    return _call(["kb", "list"])


@mcp.tool()
def agents_kb_pull(overwrite: bool = False) -> str:
    """Fetch project knowledge from the registry."""
    args = ["kb", "pull"]
    if overwrite:
        args.append("--overwrite")
    return _call(args)


@mcp.tool()
def agents_kb_push(delete: bool = False, yes: bool = False) -> str:
    """Upload changed knowledge files to the registry."""
    args = ["kb", "push"]
    if delete:
        args.append("--delete")
    if yes:
        args.append("--yes")
    return _call(args)


# --- Core ---


@mcp.tool()
def agents_core_list(path: str, bucket: str | None = None) -> str:
    """List capabilities marked core for an area (with inheritance)."""
    args = ["core", "list", path]
    if bucket:
        args.extend(["--bucket", bucket])
    return _call(args)


@mcp.tool()
def agents_core_add(path: str, name: str, bucket: str | None = None) -> str:
    """Mark a capability as core for an area."""
    args = ["core", "add", path, name]
    if bucket:
        args.extend(["--bucket", bucket])
    return _call(args)


@mcp.tool()
def agents_core_rm(path: str, name: str, bucket: str | None = None) -> str:
    """Unmark a capability as core for an area."""
    args = ["core", "rm", path, name]
    if bucket:
        args.extend(["--bucket", bucket])
    return _call(args)


# --- Escape hatch ---


@mcp.tool()
def agents_run(subcommand: str, args: list[str] | None = None) -> str:
    """Run a whitelisted agents subcommand with extra arguments."""
    cli_args = [subcommand, *(args or [])]
    return _call(cli_args)


def main() -> None:
    resolve_agents_bin()
    mcp.run()


if __name__ == "__main__":
    main()
