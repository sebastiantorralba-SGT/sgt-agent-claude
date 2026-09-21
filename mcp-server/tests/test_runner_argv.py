"""Subprocess argv safety."""

from unittest.mock import MagicMock, patch

from agents_mcp.runner import AgentsRunner


@patch("agents_mcp.runner.subprocess.run")
def test_run_uses_argv_list_not_shell(mock_run: MagicMock):
    mock_run.return_value = MagicMock(returncode=0, stdout="ok", stderr="")
    runner = AgentsRunner(agents_bin=r"C:\tools\agents.exe", workspace=r"C:\repo")
    runner.run(["search", "deploy microservice", "--area", "arquitectura"])

    mock_run.assert_called_once()
    kwargs = mock_run.call_args.kwargs
    assert kwargs.get("shell") is not True
    command = mock_run.call_args.args[0]
    assert command[0] == r"C:\tools\agents.exe"
    assert command[1:] == [
        "search",
        "deploy microservice",
        "--area",
        "arquitectura",
    ]
    assert kwargs["cwd"] == r"C:\repo"
