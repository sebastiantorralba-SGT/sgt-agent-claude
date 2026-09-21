"""Generate plugin slash command files from the plan table."""

from __future__ import annotations

from pathlib import Path

ROUTING = "Read [routing.md](references/routing.md) before executing.\n"

COMMANDS: list[tuple] = [
    (
        "agents-version",
        "Show the installed agents CLI version",
        "agents_version",
        "agents version",
        [],
        "agents version",
        False,
    ),
    (
        "agents-search",
        "Search capabilities in this repo and the shared registry",
        "agents_search",
        "agents search",
        [
            ("query", "required", "what you are about to do, in your words"),
            ("area", "optional", "filter e.g. arquitectura or bigdata/ml"),
            ("limit", "optional", "max results (default 10)"),
        ],
        'agents search "<query>" [--area <area>] [--limit N]',
        False,
    ),
    (
        "agents-list",
        "List installed capabilities or the full registry",
        "agents_list",
        "agents list",
        [
            ("area", "optional", "filter by area"),
            ("registry", "optional", "set true to list --registry"),
        ],
        "agents list [--area <area>] [--registry]",
        False,
    ),
    (
        "agents-info",
        "Show detail for a capability by name",
        "agents_info",
        "agents info",
        [("name", "required", "capability name")],
        "agents info <name>",
        False,
    ),
    (
        "agents-add",
        "Install a capability from the registry into .agents/",
        "agents_add",
        "agents add",
        [
            ("name", "required", "capability name"),
            ("version", "optional", "specific version"),
        ],
        "agents add <name> [--version <version>]",
        False,
    ),
    (
        "agents-update",
        "Update capabilities and/or the CLI (dry-run by default)",
        "agents_update",
        "agents update",
        [
            ("dry_run", "optional", "default true; set false to apply"),
            ("cli_only", "optional", "only update CLI"),
            ("force", "optional", "replace locally edited capabilities"),
        ],
        "agents update [--dry-run] [--cli] [--force]",
        True,
    ),
    (
        "agents-areas",
        "Show the area tree from the registry",
        "agents_areas",
        "agents areas",
        [],
        "agents areas",
        False,
    ),
    (
        "agents-kinds",
        "Show project kinds and what each brings",
        "agents_kinds",
        "agents kinds",
        [
            ("defaults", "optional", "use CLI defaults"),
            ("publish", "optional", "publish kinds to registry (admin)"),
        ],
        "agents kinds [--defaults] [--publish]",
        False,
    ),
    (
        "agents-taxonomy",
        "Show or publish the area taxonomy",
        "agents_taxonomy",
        "agents taxonomy",
        [
            ("defaults", "optional", "use CLI defaults when publishing"),
            ("publish", "optional", "publish taxonomy (admin)"),
        ],
        "agents taxonomy [--defaults] [--publish]",
        False,
    ),
    (
        "agents-init",
        "Seed README, AGENTS.md and .agents/ in this repo",
        "agents_init",
        "agents init",
        [
            ("profile", "optional", "python-uv | node | empty"),
            ("kind", "optional", "development | maintenance | ..."),
            ("area", "optional", "area/subarea"),
        ],
        "agents init [--profile <p>] [--kind <k>] [--area <a>]",
        True,
    ),
    (
        "agents-migrate",
        "Consolidate per-tool config into neutral structure",
        "agents_migrate",
        "agents migrate",
        [
            ("apply", "optional", "execute plan (default false)"),
            ("clean", "optional", "remove originals after migrate"),
            ("area", "optional", "target area for migrated skills"),
        ],
        "agents migrate [--apply] [--clean] [--area <a>]",
        True,
    ),
    (
        "agents-check",
        "Validate .agents/ structure",
        "agents_check",
        "agents check",
        [("strict", "optional", "treat warnings as errors")],
        "agents check [--strict]",
        False,
    ),
    (
        "agents-link",
        "Wire CLAUDE.md import, slash commands, and mcp.json copies",
        "agents_link",
        "agents link",
        [
            ("central", "optional", "link CLAUDE.md stub (default true)"),
            ("commands", "optional", "symlink commands (default true)"),
            ("mcp", "optional", "copy mcp.json (default true)"),
        ],
        "agents link [--no-central] [--no-commands] [--no-mcp]",
        False,
    ),
    (
        "agents-new",
        "Create a capability with path and frontmatter",
        "agents_new",
        "agents new",
        [
            ("kind", "required", "skill | rule | command | subagent | memory"),
            ("name", "required", "lowercase-with-hyphens"),
            ("description", "optional", "when it applies"),
            ("area", "optional", "for skills: area/subarea"),
            ("scope", "optional", "shared | project"),
        ],
        'agents new <kind> <name> -d "..." [--area <a>] [--scope shared|project]',
        False,
    ),
    (
        "agents-propose",
        "Submit a capability for area-admin review",
        "agents_propose",
        "agents propose",
        [("target_name", "required", "capability name or path")],
        "agents propose <name>",
        False,
    ),
    (
        "agents-publish",
        "Publish directly to the team registry (publisher path)",
        "agents_publish",
        "agents publish",
        [
            ("target_name", "required", "capability name or path"),
            ("scope", "optional", "shared | project"),
        ],
        "agents publish <name> [--scope shared|project]",
        True,
    ),
    (
        "agents-unpublish",
        "Retire a capability from the registry (irreversible)",
        "agents_unpublish",
        "agents unpublish",
        [
            ("name", "required", "capability name"),
            ("version", "optional", "single version to retire"),
            ("all_versions", "optional", "retire all versions"),
        ],
        "agents unpublish <name> [--version V] [--all] --yes",
        True,
    ),
    (
        "agents-kb-list",
        "Compare local knowledge with the registry",
        "agents_kb_list",
        "agents kb list",
        [],
        "agents kb list",
        False,
    ),
    (
        "agents-kb-pull",
        "Fetch project knowledge from the registry",
        "agents_kb_pull",
        "agents kb pull",
        [("overwrite", "optional", "overwrite differing local files")],
        "agents kb pull [--overwrite]",
        False,
    ),
    (
        "agents-kb-push",
        "Upload changed knowledge files to the registry",
        "agents_kb_push",
        "agents kb push",
        [("delete", "optional", "remove remote files missing locally")],
        "agents kb push [--delete]",
        True,
    ),
    (
        "agents-core-list",
        "List core capabilities for an area",
        "agents_core_list",
        "agents core list",
        [("path", "required", "area or area/subarea")],
        "agents core list <path>",
        False,
    ),
    (
        "agents-core-add",
        "Mark a capability as core for an area",
        "agents_core_add",
        "agents core add",
        [
            ("path", "required", "area or area/subarea"),
            ("name", "required", "published capability name"),
        ],
        "agents core add <path> <name>",
        False,
    ),
    (
        "agents-core-rm",
        "Unmark a capability as core for an area",
        "agents_core_rm",
        "agents core rm",
        [
            ("path", "required", "area or area/subarea"),
            ("name", "required", "capability name"),
        ],
        "agents core rm <path> <name>",
        False,
    ),
    (
        "agents-login-status",
        "Check whether a review-service token is stored locally",
        "agents_login_status",
        None,
        [],
        None,
        False,
    ),
]

AUTH_HINT_COMMANDS = {
    "agents-propose",
    "agents-kb-push",
    "agents-core-add",
    "agents-core-rm",
    "agents-publish",
}


def cli_title(slug: str) -> str:
    if slug == "agents-kb-list":
        return "agents kb list"
    if slug.startswith("agents-kb-"):
        return f"agents kb {slug.split('-')[-1]}"
    if slug.startswith("agents-core-"):
        return f"agents core {slug.split('-')[-1]}"
    return slug.replace("agents-", "agents ").replace("-", " ")


def render_command(
    slug: str,
    desc: str,
    mcp_tool: str,
    cli_cmd: str | None,
    inputs: list[tuple[str, str, str]],
    shell_example: str | None,
    needs_confirm: bool,
) -> str:
    lines = [
        "---",
        f"name: {slug}",
        f"description: {desc}",
        "---",
        "",
        f"# {cli_title(slug)}",
        "",
        ROUTING,
        "## Prerequisite",
        "",
        "Read `AGENTS.md` at the repo root (see routing.md). Do not call MCP or shell until read.",
        "",
        "## Input",
        "",
    ]
    if inputs:
        for name, req, hint in inputs:
            lines.append(f"- **{name}** ({req}): {hint}")
        lines.append("")
        lines.append("If required input is missing, ask once.")
    else:
        lines.append("- No arguments required.")
    lines.append("")

    lines.extend(["## Execute", ""])
    if needs_confirm:
        lines.append(
            "**Confirm with the user first** (see routing.md). "
            "For MCP, pass `confirm=true` or `yes=true` only after approval."
        )
        lines.append("")

    lines.append(f"1. **MCP (preferred):** call `{mcp_tool}` with the arguments above.")
    if shell_example:
        lines.append(f"2. **Shell fallback** from workspace root: `{shell_example}`")
    elif cli_cmd:
        lines.append(f"2. **Shell fallback** from workspace root: `{cli_cmd}`")
    else:
        lines.append("2. **Shell fallback:** not applicable — use MCP only.")
    lines.append("")

    lines.extend(["## Output", ""])
    lines.append("- Show stdout or MCP JSON in the reply.")
    lines.append("- On auth errors, tell the user to run `agents login` in a terminal.")
    if slug in AUTH_HINT_COMMANDS:
        lines.append("- On missing `.agents/`, suggest `/agents-init` first.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "commands"
    out.mkdir(exist_ok=True)

    for entry in COMMANDS:
        slug = entry[0]
        content = render_command(*entry)
        (out / f"{slug}.md").write_text(content, encoding="utf-8")
        print(f"wrote {slug}")

    print(f"done {len(COMMANDS)}")


if __name__ == "__main__":
    main()
