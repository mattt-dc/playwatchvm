#!/bin/bash

# Update and upgrade the system
sudo apt-get update
sudo apt-get upgrade -y

# Install the Ubuntu desktop environment
sudo apt-get install -y ubuntu-desktop

# Install Python's package installer pip
sudo apt-get install -y python3-pip

sudo apt-get install -y python3-tk python3-dev

sudo apt-get install -y ffmpeg

(crontab -l 2>/dev/null; echo "@reboot python3 /home/vagrant/automation.py") | crontab -

# Optional: Install additional RetroArch cores
# sudo apt-get install retroarch-* -y
