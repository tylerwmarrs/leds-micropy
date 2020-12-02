import math
import random
import time

import machine
import neopixel

from utils import (
    randrange,
    clear,
    adjust_brightness,
    read_file_and_display
)

"""
Cycles through various Mario images randomly based on configuration variables
listed below. The images displayed assume a 16 x 16 matrix, but should work on
anything larger; just not smaller.
"""

# Rows in the matrix
rows = 16

# Cols in the matrix
cols = 16

# Data pin hooked up to the controller
pin = 2

# Brightness as a decimal percent from 0 to 1
brightness = 0.02

# Sleep time between the main loop
wait_time = 0.1

# Number of seconds that must pass before cycling the image
reset_time = 3

# The image data to display.
# These are assumed to be uploaded to the microcontroller already.
files = [
    'retro_mario2.txt',
    'retro_question_block.txt',
    'retro_1up.txt',
    'retro_star.txt',
    'retro_flower.txt'
]

def main():
    np = neopixel.NeoPixel(machine.Pin(pin), rows * cols)
    clear(np)
    elapsed = 0

    while True:
        index = randrange(len(files))
        art = files[index]
        read_file_and_display(art, np, brightness)
        time.sleep(wait_time)
        elapsed += wait_time

        if elapsed >= reset_time:
            elapsed = 0
            clear(np)

if __name__ == '__main__':
    main()