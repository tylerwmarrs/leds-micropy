import math
import random

def randrange(start, stop=None):
    """
    Provides a random integer betwen start and stop. It is not inclusive of
    stop.

    Parameters
    ----------
    start : int
        Starting integer.
    stop : int
        Stopping integer.
    
    Returns
    -------
    number : int
        A number between start and stop.
    """
    if stop is None:
        stop = start
        start = 0
    upper = stop - start
    bits = 0
    pwr2 = 1
    while upper > pwr2:
        pwr2 <<= 1
        bits += 1
    while True:
        r = random.getrandbits(bits)
        if r < upper:
            break

    return r + start

def random_color(brightness=0.25):
    """
    Generates a random brightness corrected color as an R,G,B tuple.

    Parameters
    ----------
    brightness : float, default=0.25
        A decimal percentage between 0 and 1.
    
    Returns
    -------
    random_rgb : tuple
        A tuple of random RGB integer values.
    """
    return tuple([math.ceil(randrange(256) * brightness) for _ in range(3)])

def adjust_brightness(np, brightness):
    """
    Adjusts the brightness of all existing colors written to the NeoPixel
    instance that is passed in.

    Parameters
    ----------
    np : neopixel.NeoPixel
        The NeoPixel instance.
    brightness : float
        A decimal percentage between 0 and 1.
    
    Returns
    -------
    None
    """
    for i in range(np.n):
        color = tuple([math.ceil(brightness * c) for c in np[i]])
        np[i] = color
    np.write()

def clear(np):
    """
    Clears all of the pixels for the given NeoPixel instance. Essentially,
    it shuts all of the pixels off/setting them to black.

    Parameters
    ----------
    np : neopixel.NeoPixel
        The NeoPixel instance.
    
    Returns
    -------
    None
    """
    np.fill((0, 0, 0))
    np.write()

def read_file_and_display(file, np, brightness=0.25):
    """
    Reads a file formatted as R,G,B values per line and displays them on the
    NeoPixel instance. The colors are brightness corrected to 25% by default
    before displaying the file.

    Parameters
    ----------
    file : str
        The file path to read.
    np : neopixel.NeoPixel
        The NeoPixel instance.
    brightness : float, default=0.25
        A decimal percentage between 0 and 1.
    
    Returns
    -------
    None
    """
    with open(file) as f:
        i = 0
        for line in f:
            color = tuple(line.strip().split(','))
            adjusted_color = tuple([math.ceil(brightness * int(c)) for c in color])
            np[i] = adjusted_color
            i += 1
        
        np.write()