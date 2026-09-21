"""Whitelist enforcement for agents_run."""

import pytest

from agents_mcp.runner import ALLOWED_SUBCOMMANDS, AgentsRunner


def test_allowed_subcommands_include_core_workflow():
    assert "search" in ALLOWED_SUBCOMMANDS
    assert "kb" in ALLOWED_SUBCOMMANDS
    assert "login" not in ALLOWED_SUBCOMMANDS
    assert "logout" not in ALLOWED_SUBCOMMANDS
    assert "release" not in ALLOWED_SUBCOMMANDS


def test_validate_rejects_unknown_subcommand():
    runner = AgentsRunner(agents_bin="agents", workspace=".")
    with pytest.raises(ValueError, match="not allowed"):
        runner.validate_subcommand("login")


def test_run_rejects_empty_args():
    runner = AgentsRunner(agents_bin="agents", workspace=".")
    with pytest.raises(ValueError, match="At least one"):
        runner.run([])
