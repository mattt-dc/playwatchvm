import pyautogui
import time
import os
import subprocess

# Path to the shell script
minetest_binary_path = '/home/vagrant/minetest/bin/minetest'

# Check if the Minetest binary exists
if not os.path.exists(minetest_binary_path):
    print("Minetest binary not found. Running the script to compile Minetest.")
    subprocess.run(['bash', '/home/vagrant/minetest-compile.sh'])
else:
    print("Minetest binary found. Proceeding with launch.")

# Start Minetest
time.sleep(10)
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)
pyautogui.write('./minetest/bin/minetest')
pyautogui.press('enter')

# Wait for Minetest to start
time.sleep(5)

# Press the down arrow to go to the next menu option
pyautogui.press('down')