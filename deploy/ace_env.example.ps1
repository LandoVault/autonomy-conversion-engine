# Example: point ACE at this machine's store folders (persistent, current user only).
# Copy, edit the three paths, then run it once in PowerShell. Open a NEW terminal afterwards.
# The engine, loops, backup script and deploy scripts all read these variables; unset = reference paths.
# Keep the three stores in three separate folders, none inside another, on local disks.
[Environment]::SetEnvironmentVariable('ACE_STORE', 'D:\ACE\ACE_storage', 'User')  # control plane (git; remote optional, PRIVATE only)
[Environment]::SetEnvironmentVariable('ACE_LOCAL', 'D:\ACE\ACE_local',   'User')  # content plane (git; NEVER a remote)
[Environment]::SetEnvironmentVariable('ACE_HUB',   'D:\ACE\ACE_hub',     'User')  # Obsidian hub vault (local)
# Optional: default backup destination for engine/backup_ace.ps1 (local/offline media only)
# [Environment]::SetEnvironmentVariable('ACE_BACKUP', 'E:\ACE_backup', 'User')
Write-Output 'ACE paths set for the current user - open a new terminal, then: python deploy\bootstrap_stores.py'
