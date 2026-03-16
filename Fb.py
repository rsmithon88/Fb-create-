import os
import sys
import uuid
import time
import platform
import datetime

# ===== SETTINGS ===== #

ALLOWED_ID = "PUT_DEVICE_ID_HERE"
EXPIRE_DATE = "2026-12-31"

modules = ["requests","bs4","mechanize","pyotp"]

# ===== DEVICE ID ===== #

def get_id():
    return str(uuid.getnode())

device_id = get_id()

# ===== LOCK SYSTEM ===== #

if device_id != ALLOWED_ID:
    print("\033[1;91m[!] SCRIPT LOCKED")
    print("\033[1;93mDEVICE ID :", device_id)
    print("\033[1;92mSEND THIS ID TO ADMIN")
    sys.exit()

# ===== EXPIRE CHECK ===== #

today = datetime.date.today()
exp = datetime.datetime.strptime(EXPIRE_DATE,"%Y-%m-%d").date()

if today > exp:
    print("\033[1;91m[!] SCRIPT EXPIRED")
    sys.exit()

# ===== DEVICE CHECK ===== #

bit = platform.architecture()[0]

if bit != "64bit":
    print("\033[1;91m[!] ONLY 64 BIT DEVICE SUPPORTED")
    sys.exit()

print("\033[1;92m[✓] DEVICE APPROVED")
time.sleep(1)

# ===== AUTO UPDATE ===== #

try:
    os.system("git pull --quiet")
except:
    pass

# ===== MODULE INSTALL ===== #

for m in modules:
    try:
        __import__(m)
    except:
        print(f"[+] Installing {m}")
        os.system(f"pip install {m}")

# ===== CLEAR SCREEN ===== #

os.system("clear")

print("\033[1;96m[✓] LOADING MAIN SCRIPT...\n")
time.sleep(1)

# ===== MAIN SCRIPT ===== #

import AUTO
