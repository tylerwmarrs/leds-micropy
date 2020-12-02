#!/bin/bash
set -e

ampy --port /dev/ttyUSB0 --baud 115200 put main.py
ampy --port /dev/ttyUSB0 --baud 115200 put retro_mario2.txt
ampy --port /dev/ttyUSB0 --baud 115200 put retro_question_block.txt
ampy --port /dev/ttyUSB0 --baud 115200 put retro_1up.txt
ampy --port /dev/ttyUSB0 --baud 115200 put retro_star.txt
ampy --port /dev/ttyUSB0 --baud 115200 put retro_flower.txt
ampy --port /dev/ttyUSB0 --baud 115200 put ../modules/utils.py
