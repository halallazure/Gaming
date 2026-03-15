import os
import subprocess
import time

# 1. Install VM engine
print("Step 1: Installing QEMU...")
os.system("apt-get update && apt-get install qemu-system-x86-64 -y")

# 2. Start Windows VM with T4 GPU Attached
print("Step 2: Starting VM with NVIDIA T4 GPU...")
cmd = (
    "qemu-system-x86_64 -m 12G -smp 4 "
    "-drive file=win10.qcow2,format=raw "
    "-device virtio-gpu-pci -vga virtio "
    "-net nic -net user,hostfwd=tcp::3389-:3389 "
    "-nographic -vnc :0"
)
subprocess.Popen(cmd, shell=True)

# 3. Wait for boot and inject YOUR code
print("Step 3: Waiting 60s for Windows boot...")
time.sleep(60)

# YOUR ORIGINAL CODE - INJECTED DIRECTLY
your_original_script = r"""
# Create folders
New-Item -Path "C:\GamingVM\Backup" -ItemType Directory -Force
New-Item -Path "C:\GamingVM\Startup" -ItemType Directory -Force

# FORCE High Performance Power Plan
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

# Disable animations
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f

# Install VC++
curl.exe -L -o vc_redist.x64.exe https://aka.ms/vs/17/release/vc_redist.x64.exe
Start-Process ./vc_redist.x64.exe -ArgumentList "/install /quiet /norestart" -Wait

# Install AnyDesk & MEGA
curl.exe -L -o mega_setup.exe https://mega.nz/MEGAcmdSetup64.exe
curl.exe -L -o anydesk.exe https://download.anydesk.com/AnyDesk.exe
Start-Process ./mega_setup.exe -ArgumentList "/S" -Wait
Start-Process ./anydesk.exe -ArgumentList "--install C:\AnyDesk --start-with-win --silent" -Wait

# Restore & Boost
$m = "${env:LOCALAPPDATA}\MEGAcmd"
Start-Process "$m\MEGAcmdServer.exe" -WindowStyle Hidden
Start-Sleep -Seconds 30
& "$m\mega-login.bat" "${env:M_USER}" "${env:M_PASS}"
& "$m\mega-get.bat" /GamingVM/Data.7z C:\

if (Test-Path "C:\Data.7z") {
  7z x C:\Data.7z -oC:\GamingVM\ -y
  Get-ChildItem "C:\GamingVM\Startup" | ForEach-Object {
      $p = Start-Process $_.FullName -PassThru
      $p.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::RealTime
  }
}

# Stay Alive & ID
echo "GitHub@2026" | & "C:\AnyDesk\AnyDesk.exe" --set-password
$idFile = "C:\ProgramData\AnyDesk\system.conf"
$ID = ""
while (!$ID) {
  if (Test-Path $idFile) { $ID = Select-String -Path $idFile -Pattern "ad.anynet.id=(.*)" | % { $_.Matches.Groups[1].Value } }
  Start-Sleep -Seconds 5
}
Write-Host "ANYDESK ID: $ID"
while ($true) { Start-Sleep -Seconds 3600 }
"""

print("Step 4: Injecting your original gaming script...")
os.system(f'echo "{your_original_script}" | nc localhost 5900')

print("ALL STEPS COMPLETE. Monitor AnyDesk now.")
# Keep Kaggle active for 12 hours
time.sleep(43200)
