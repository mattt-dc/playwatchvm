import pyautogui
import time
import os
import subprocess
import random
import string

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

# Create new world
pyautogui.moveTo(800,490)
pyautogui.click()
random_world_name = ''.join(random.choices(string.ascii_letters, k=10))
pyautogui.write(random_world_name)
pyautogui.moveTo(450,600)
pyautogui.click()
pyautogui.moveTo(700,520)
pyautogui.click()

time.sleep(5)

output_file = '/home/vagrant/Videos/' + random_world_name + '.mp4'
command = f"ffmpeg -y -f x11grab -video_size 957x713 -i :0.0+67,55 -codec:v libx264 {output_file}"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(3)
process.terminate()
process.wait()