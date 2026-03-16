import os
import sys
import time

# ===== KEY SYSTEM ===== #

KEY = "MITHON-123"

print("\033[1;96m==============================")
print("        TOOL KEY SYSTEM")
print("==============================")

user_key = input("ENTER KEY : ")

if user_key != KEY:
    print("\033[1;91mWRONG KEY!")
    sys.exit()

print("\033[1;92mKEY ACCEPTED")
time.sleep(1)

# ===== MODULE CHECK ===== #

modules = ["requests","bs4","mechanize","pyotp"]

for m in modules:
    try:
        __import__(m)
    except:
        os.system(f"pip install {m}")

# ===== CLEAR SCREEN ===== #

os.system("clear")

print("\033[1;96mSTARTING MAIN SCRIPT...\n")
time.sleep(1)

# ===== MAIN SCRIPT ===== #

import AUTO
