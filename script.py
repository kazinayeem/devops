import os
import platform
import shutil

print("===== SYSTEM INFO =====")
print(f"OS           : {platform.system()} {platform.release()}")
print(f"Architecture : {platform.machine()}")
print(f"Processor    : {platform.processor()}")

# CPU
cpu_count = os.cpu_count()
print("\n===== CPU INFO =====")
print(f"Total Cores  : {cpu_count}")

# RAM
print("\n===== RAM INFO =====")
with open("/proc/meminfo") as f:
    meminfo = f.read()

mem_total = int([line for line in meminfo.split("\n") if "MemTotal" in line][0].split()[1]) // 1024
mem_free = int([line for line in meminfo.split("\n") if "MemAvailable" in line][0].split()[1]) // 1024

print(f"Total RAM    : {mem_total} MB")
print(f"Available    : {mem_free} MB")

# Disk / ROM
print("\n===== DISK INFO =====")
disk = shutil.disk_usage("/")
print(f"Total Disk   : {disk.total // (1024**3)} GB")
print(f"Used Disk    : {disk.used // (1024**3)} GB")
print(f"Free Disk    : {disk.free // (1024**3)} GB")
