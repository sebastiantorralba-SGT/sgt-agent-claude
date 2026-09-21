"""Subprocess wrapper for the agents CLI with a command whitelist."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict, dataclass
from typing import Any

from .bootstrap import resolve_agents_bin, resolve_workspace

ALLOWED_SUBCOMMANDS = frozenset(
    {
        "version",
        "search",
        "list",
        "info",
        "add",
        "update",
        "areas",
        "kinds",
        "taxonomy",
        "init",
        "migrate",
        "check",
        "link",
        "new",
        "propose",
        "publish",
        "unpublish",
        "kb",
        "core",
    }
)

RUN_TIMEOUT_SECONDS = 600


@dataclass
class CommandResult:
    exit_code: int
    stdout: str
    stderr: str
    command: list[str]
    workspace: str

    @property
    def ok(self) -> bool:
        return self.exit_code == 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


class AgentsRunner:
    def __init__(self, *, agents_bin: str | None = None, workspace: str | None = None):
        self._agents_bin = agents_bin
        self._workspace = workspace

    @property
    def agents_bin(self) -> str:
        if self._agents_bin:
            return self._agents_bin
        return str(resolve_agents_bin())

    @property
    def workspace(self) -> str:
        if self._workspace:
            return self._workspace
        return str(resolve_workspace())

    def validate_subcommand(self, subcommand: str) -> None:
        if subcommand not in ALLOWED_SUBCOMMANDS:
            allowed = ", ".join(sorted(ALLOWED_SUBCOMMANDS))
            raise ValueError(
                f"Subcommand {subcommand!r} is not allowed. Allowed: {allowed}"
            )

    def run(self, args: list[str]) -> CommandResult:
        if not args:
            raise ValueError("At least one CLI argument is required.")
        self.validate_subcommand(args[0])
        command = [self.agents_bin, *args]
        completed = subprocess.run(
            command,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            check=False,
            timeout=RUN_TIMEOUT_SECONDS,
        )
        return CommandResult(
            exit_code=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
            command=command,
            workspace=self.workspace,
        )

    def format(self, result: CommandResult) -> str:
        payload = result.to_dict()
        payload["ok"] = result.ok
        return json.dumps(payload, indent=2)


def require_confirmation(*, confirmed: bool, action: str) -> None:
    if not confirmed:
        raise ValueError(
            f"{action} requires explicit confirmation. Pass confirm=true."
        )
