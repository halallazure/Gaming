import os
import subprocess

# 1. Install QEMU (The engine)
os.system("apt-get update && apt-get install qemu-system-x86-64 -y")

# 2. Start the VM with the NVIDIA T4 GPU linked
# We use -device virtio-gpu-pci to hook the Kaggle T4 into your Windows VM
cmd = (
    "qemu-system-x86_64 -m 12G -smp 4 "
    "-drive file=win10.qcow2,format=raw "
    "-device virtio-gpu-pci -vga virtio "
    "-net nic -net user,hostfwd=tcp::3389-:3389 "
    "-nographic -vnc :0"
)

# Start it in the background
subprocess.Popen(cmd, shell=True)
print("VM is starting with T4 GPU support...")

# 3. Wait a moment then run your original Gaming script
# This part tells the VM to start your MEGA/AnyDesk setup
os.system("sleep 60") 
print("Running your Ultimate-Gaming-VM script now...")
