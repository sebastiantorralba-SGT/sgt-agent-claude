#Requires -Version 5.1
$ErrorActionPreference = "Stop"

$GitSpec = if ($env:AGENTS_GIT_SPEC) { $env:AGENTS_GIT_SPEC } else {
    "agents @ git+https://git.seguritech.org:92/bigdata-seguritech/code-template.git"
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "uv is not on PATH. Install it from https://docs.astral.sh/uv/"
}

$agentsCmd = Get-Command agents -ErrorAction SilentlyContinue
if ($agentsCmd) {
    Write-Host "agents already installed: $(agents version)"
    exit 0
}

$localBin = Join-Path $env:USERPROFILE ".local\bin\agents.exe"
if (Test-Path $localBin) {
    Write-Host "agents found at $localBin: $(& $localBin version)"
    exit 0
}

Write-Host "Installing agents via uv tool install..."
& uv tool install $GitSpec
Write-Host "Installed: $(agents version)"
Write-Host "Run 'agents login' in a terminal before propose, kb push, or core writes."
