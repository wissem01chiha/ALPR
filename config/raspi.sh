#!/bin/bash

echo "installing LPDR software on raspberrypi..."

sudo apt get update
sudo apt upgrade 

pip install --upgrade pip setuptools wheel
sudo apt install libatlas-base-dev gfortran
sudo apt install python3-opencv libopencv-dev

# Package the code into a single standlone executable
sudo pip install pyinstaller











