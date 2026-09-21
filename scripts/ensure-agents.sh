#!/usr/bin/env bash
set -euo pipefail

GIT_SPEC="${AGENTS_GIT_SPEC:-agents @ git+https://git.seguritech.org:92/bigdata-seguritech/code-template.git}"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is not on PATH. Install it from https://docs.astral.sh/uv/" >&2
  exit 1
fi

if command -v agents >/dev/null 2>&1; then
  echo "agents already installed: $(agents version)"
  exit 0
fi

LOCAL_BIN="${HOME}/.local/bin/agents"
if [[ -x "${LOCAL_BIN}" ]]; then
  echo "agents found at ${LOCAL_BIN}: $("${LOCAL_BIN}" version)"
  exit 0
fi

echo "Installing agents via uv tool install..."
uv tool install "${GIT_SPEC}"
echo "Installed: $(agents version)"
echo "Run 'agents login' in a terminal before propose, kb push, or core writes."
