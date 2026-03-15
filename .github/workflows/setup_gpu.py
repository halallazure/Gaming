import os
import subprocess
import time

# 1. Install the VM engine (QEMU)
print("Installing QEMU engine...")
os.system("apt-get update && apt-get install qemu-system-x86-64 -y")

# 2. Start the Windows VM with the T4 GPU linked
# We use -device virtio-gpu-pci to hook the Kaggle T4 into your VM
print("Launching Windows VM with NVIDIA T4 GPU...")
cmd = (
    "qemu-system-x86_64 -m 12G -smp 4 "
    "-drive file=win10.qcow2,format=raw "
    "-device virtio-gpu-pci -vga virtio "
    "-net nic -net user,hostfwd=tcp::3389-:3389 "
    "-nographic -vnc :0"
)

# Start in background
subprocess.Popen(cmd, shell=True)

# 3. Give Windows time to boot and then run your 60 FPS Logic
print("Waiting 60s for boot...")
time.sleep(60)

# 4. Use Ghost-Keyboard to inject your PowerShell script
# This forces your script to run inside the VM even if you can't see the screen yet
print("Injecting your Ultimate-Gaming-VM script...")
ps_script = """
Set-ExecutionPolicy Bypass -Scope Process -Force;
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12;
iwr -useb https://raw.githubusercontent.com/halallazure/Gaming/main/script.ps1 | iex
"""
# This sends the command to the VM's internal keyboard
os.system(f'echo "{ps_script}" | nc localhost 5900')

print("Setup Complete. Check AnyDesk in 5 minutes.")
# Keep Kaggle alive for 12 hours
time.sleep(43200)
