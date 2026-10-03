# Registers the daily ACE backup (engine/backup_ace.ps1) in Windows Task Scheduler - the only loop a fresh
# deployment schedules. The `ace tick` loop is NOT registered here: it is gated on the owner's ruling R5-2
# (spec/10) and is not built yet. Refuses to replace an existing task (never overwrite).
# Usage (as the deploying user):  .\deploy\register_backup_task.ps1 -BackupDest 'E:\ACE_backup' [-At '18:00']
# The backup destination must be local or offline media (spec/11: no cloud-touching backup without a ruling).
param(
    [Parameter(Mandatory = $true)][string]$BackupDest,
    [string]$At = '18:00',
    [string]$TaskName = 'ACE_backup_daily'
)
$ErrorActionPreference = 'Stop'
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Write-Output "REFUSED: task '$TaskName' already exists - inspect it in Task Scheduler; this script never replaces it."; exit 1
}
$script = Join-Path (Split-Path -Parent $PSScriptRoot) 'engine\backup_ace.ps1'
if (-not (Test-Path $script)) { throw "backup script not found: $script" }
$action  = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`" -Dest `"$BackupDest`""
$trigger = New-ScheduledTaskTrigger -Daily -At $At
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Description 'ACE daily backup: content plane + hub vault mirrored, git bundles of repo and control plane (never deletes).' | Out-Null
Write-Output "registered '$TaskName' daily at $At -> $BackupDest (store paths come from ACE_LOCAL / ACE_HUB / ACE_STORE)"
