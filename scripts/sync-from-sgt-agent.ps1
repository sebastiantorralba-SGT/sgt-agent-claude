# Sync shared assets from the Cursor plugin (sgt-agent) into this Claude plugin repo.
param(
    [string]$Source = (Resolve-Path (Join-Path $PSScriptRoot "..\..\sgt-agent")).Path,
    [switch]$IncludeManifests
)

$ErrorActionPreference = "Stop"
$dest = Split-Path $PSScriptRoot -Parent

if (-not (Test-Path $Source)) {
    throw "Source not found: $Source"
}

Write-Host "Syncing from $Source to $dest"

robocopy (Join-Path $Source "mcp-server") (Join-Path $dest "mcp-server") /E /XD .venv __pycache__ .pytest_cache /NFL /NDL /NJH /NJS | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy mcp-server failed with exit $LASTEXITCODE" }

Copy-Item (Join-Path $Source "scripts\ensure-agents.ps1") (Join-Path $dest "scripts\") -Force
Copy-Item (Join-Path $Source "scripts\ensure-agents.sh") (Join-Path $dest "scripts\") -Force
Copy-Item (Join-Path $Source "scripts\generate_commands.py") (Join-Path $dest "scripts\") -Force
Copy-Item (Join-Path $Source "LICENSE") $dest -Force

if ($IncludeManifests) {
    Write-Warning "Overwriting Claude manifests is unusual; review diffs before commit."
}

Push-Location $dest
try {
    python scripts/generate_claude_commands.py
} finally {
    Pop-Location
}

Write-Host "Done. Review skills/bootstrap and commands/references/routing.md manually if sgt-agent changed them."
