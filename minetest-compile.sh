#!/bin/bash

# Install dependencies for Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y g++ make libc6-dev cmake libpng-dev libjpeg-dev libxi-dev libgl1-mesa-dev libsqlite3-dev libogg-dev libvorbis-dev libopenal-dev libcurl4-gnutls-dev libfreetype6-dev zlib1g-dev libgmp-dev libjsoncpp-dev libzstd-dev libluajit-5.1-dev git

# Clone Minetest and Minetest Game repositories
git clone --depth 1 https://github.com/minetest/minetest.git
cd minetest
git clone --depth 1 https://github.com/minetest/minetest_game.git games/minetest_game

# Clone IrrlichtMt
git clone --depth 1 https://github.com/minetest/irrlicht.git lib/irrlichtmt

# Compile Minetest
cmake . -DRUN_IN_PLACE=TRUE
make -j$(nproc)