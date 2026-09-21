"""Smoke tests for MCP tool registration."""

import agents_mcp.server as server_module


def test_mcp_server_has_expected_tools():
    tool_names = {tool.name for tool in server_module.mcp._tool_manager.list_tools()}
    expected = {
        "agents_version",
        "agents_search",
        "agents_list",
        "agents_info",
        "agents_add",
        "agents_update",
        "agents_check",
        "agents_propose",
        "agents_kb_list",
        "agents_run",
        "agents_login_status",
    }
    assert expected.issubset(tool_names)


def test_require_confirmation_blocks_without_flag():
    from agents_mcp.runner import require_confirmation

    try:
        require_confirmation(confirmed=False, action="test")
        raised = False
    except ValueError:
        raised = True
    assert raised
