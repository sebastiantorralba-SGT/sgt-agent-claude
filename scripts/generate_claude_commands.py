"""Generate Claude Code plugin commands from the shared command table."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_commands import AUTH_HINT_COMMANDS, COMMANDS, cli_title, render_command

PLUGIN_NAMESPACE = "agents"
ROUTING = "Read [routing.md](references/routing.md) before executing.\n"


def to_claude_slash(slug: str) -> str:
    return f"/{PLUGIN_NAMESPACE}:{slug}"


def adapt_body_for_claude(content: str) -> str:
    lines = content.splitlines()
    adapted: list[str] = []
    for line in lines:
        if line.startswith("name: "):
            continue
        if line.startswith("description: "):
            adapted.append("description: " + line.split("description: ", 1)[1])
            adapted.append("disable-model-invocation: true")
            continue
        line = re.sub(
            r"`/agents-([a-z0-9-]+)`",
            lambda match: f"`{to_claude_slash('agents-' + match.group(1))}`",
            line,
        )
        line = line.replace("/agents-init", to_claude_slash("agents-init"))
        line = line.replace("/agents-*", f"/{PLUGIN_NAMESPACE}:agents-*")
        adapted.append(line)
    return "\n".join(adapted) + "\n"


def render_claude_command(*entry) -> str:
    content = render_command(*entry)
    return adapt_body_for_claude(content)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "commands"
    out.mkdir(exist_ok=True)

    for entry in COMMANDS:
        slug = entry[0]
        content = render_claude_command(*entry)
        (out / f"{slug}.md").write_text(content, encoding="utf-8")
        print(f"wrote {slug}")

    print(f"done {len(COMMANDS)}")


if __name__ == "__main__":
    main()
