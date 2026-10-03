# ACE backup loop - default target per ruling R3-4 (2026-07-19): G:\ACE_backup (local backup)
# Backs up: content plane (ACE_local), hub vault (ACE_hub), and git bundles of ACE + ACE_storage.
# Never deletes: robocopy WITHOUT /MIR (adds/updates only, per the never-delete rule); dated bundle files.
# Run manually or via Windows Task Scheduler (recommended: daily).
# Paths default to the reference deployment; another machine overrides them with -Parameters or the
# ACE_BACKUP / ACE_LOCAL / ACE_HUB / ACE_STORE environment variables (deploy/README.md). The repo is this script's parent.
param(
    [string]$Dest  = $(if ($env:ACE_BACKUP) { $env:ACE_BACKUP } else { 'G:\ACE_backup' }),
    [string]$Local = $(if ($env:ACE_LOCAL)  { $env:ACE_LOCAL }  else { 'F:\ACE_local' }),
    [string]$Hub   = $(if ($env:ACE_HUB)    { $env:ACE_HUB }    else { 'F:\ACE_hub' }),
    [string]$Store = $(if ($env:ACE_STORE)  { $env:ACE_STORE }  else { 'F:\git\ACE_storage' }),
    [string]$Repo  = (Split-Path -Parent $PSScriptRoot)
)
$ErrorActionPreference = 'Stop'
$dest = $Dest
$stamp = Get-Date -Format 'yyyy-MM-dd'
New-Item -ItemType Directory -Force -Path "$dest\ACE_local", "$dest\ACE_hub", "$dest\bundles" | Out-Null

robocopy $Local "$dest\ACE_local" /E /R:1 /W:1 /XD .git /NFL /NDL /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy ACE_local failed: $LASTEXITCODE" }
robocopy $Hub "$dest\ACE_hub" /E /R:1 /W:1 /XD .git /NFL /NDL /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy ACE_hub failed: $LASTEXITCODE" }

git -C $Local bundle create "$dest\bundles\ACE_local_$stamp.bundle"   --all
git -C $Hub   bundle create "$dest\bundles\ACE_hub_$stamp.bundle"     --all
git -C $Repo  bundle create "$dest\bundles\ACE_$stamp.bundle"         main
git -C $Store bundle create "$dest\bundles\ACE_storage_$stamp.bundle" --all

"backup OK $stamp $(Get-Date -Format HH:mm)" | Add-Content "$dest\backup_log.txt"
Write-Output "ACE backup complete -> $dest"
