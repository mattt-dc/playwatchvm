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

def WriteActionsToTextFile(random_world_name, performed_actions):
    filename = "/home/vagrant/shared/ActionLogs/" + random_world_name + "-1"
    with open(filename + '.txt', 'w') as file:
        for action in performed_actions:
            file.write(action + '\n')

def rotate_camera_left():
    pyautogui.moveRel(-100, 0, duration=0.2)
    return "rotate_camera_left"

def rotate_camera_right():
    pyautogui.moveRel(100, 0, duration=0.2)
    return "rotate_camera_right"

def press_and_hold(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def start_recording(filename):
    output_file = f'/home/vagrant/shared/Videos/{filename}.mp4'
    command = f"ffmpeg -y -f x11grab -video_size 957x713 -i :0.0+67,55 -codec:v libx264 {output_file}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def stop_recording(process):
    process.terminate()
    process.wait()

def record_first_screen(filename, length):
    process = start_recording(filename)
    time.sleep(length)
    stop_recording(process)

actions = {
    'w (forward)': lambda: press_and_hold('w', 0.2),
    'a (left)': lambda: press_and_hold('a', 0.2),
    'd (right)': lambda: press_and_hold('d', 0.2),
    'left_click (action)': lambda: pyautogui.click(),
    'rotate_camera_left (look left)': rotate_camera_left,
    'rotate_camera_right (look right)': rotate_camera_right,
}

record_first_screen(random_world_name, 3)

recording_process = start_recording(random_world_name + "-1")
performed_actions = []
for i in range(10):
    action_key = random.choice(list(actions.keys()))
    actions[action_key]()
    performed_actions.append(action_key)
    time.sleep(1)
stop_recording(recording_process)
WriteActionsToTextFile(random_world_name, performed_actions)