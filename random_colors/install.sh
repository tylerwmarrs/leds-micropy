#!/bin/bash
set -e

ampy --port /dev/ttyUSB0 --baud 115200 put main.py
ampy --port /dev/ttyUSB0 --baud 115200 put ../modules/utils.py
ampy --port /dev/ttyUSB0 --baud 115200 put ../modules/pixelmatrix.py
