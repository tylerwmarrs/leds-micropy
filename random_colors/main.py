import math
import random
import time

from pixelmatrix import PixelMatrix
from utils import (
    randrange,
    random_color
)

"""
Places random brightness corrected colors on the matrix. It clears the screen
after reset_time is hit and places a color after each wait_time.
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

# Number of seconds that must pass before clearing the matrix
reset_time = 30

def main():
    pm = PixelMatrix(pin, rows, cols)
    pm.clear()
    elapsed = 0

    while True:
        row = randrange(rows)
        col = randrange(cols)
        pm[(row, col)] = random_color(brightness=brightness)
        pm.write()
        time.sleep(wait_time)
        elapsed += wait_time

        if elapsed >= reset_time:
            elapsed = 0
            pm.clear()


if __name__ == '__main__':
    main()