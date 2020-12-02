import machine
import neopixel

class PixelMatrix(object):
    """
    A proxy class for the NeoPixel library that provides 2D mapping of the
    underly 1D array. It makes it more convenient to understand row and column
    mapping instead of trying to map each index to the correct location. Since
    a pixel matrix is wired in a zig zag pattern, it makes mapping coordinates
    much easier.

    It also provides some convenience functions that the NeoPixel library does
    not include.
    """
    def __init__(self, pin, rows, cols):
        self.rows = rows
        self.cols = cols
        self.n = rows * cols
        self.np = neopixel.NeoPixel(machine.Pin(pin), self.n)
        
    def _row_col_to_index(self, row, col):               
        r_by_c = '{}x{}'.format(self.rows, self.cols)
        
        if row >= self.rows:
            raise ValueError('row index out of range {}'.format(r_by_c))
        
        if col >= self.cols:
            raise ValueError('col index out of range {}'.format(r_by_c))
        
        is_even_row = row % 2 == 0
    
        if is_even_row:
            idx = row * self.cols + col
        else:
            idx = (row * self.cols) + (self.cols - col) - 1
        
        return idx
    
    def __setitem__(self, index, val):
        if not isinstance(index, tuple):
            raise ValueError('index must be a tuple (row, col)')
        
        internal_index = self._row_col_to_index(index[0], index[1])
        self.np[internal_index] = val

    def __getitem__(self, index):
        if not isinstance(index, tuple):
            raise ValueError('index must be a tuple (row, col)')
        
        internal_index = self._row_col_to_index(index[0], index[1])
        return self.np[internal_index]
    
    def fill(self, color):
        for i in range(self.n):
            self.np[i] = color

    def write(self):
        self.np.write()

    def clear(self):
        black = (0, 0, 0)
        self.fill(black)
        self.write()