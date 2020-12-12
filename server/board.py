"""
Represents the state of the drawing board
"""

class Board(object): 
    """
    Will be a grid with 1 pixelso where 
    you click it will fill in the square 
    with the specified color
    """
    ROWS = COLS = 720

    def __init__(self):
        self.data = self._create_empty_board()

    def update(self, x ,y, color): 
        """
        update 1 pixel (if someone clicks the pixel)
        """
        self.data[y][x] = color

    def clear(self):
        self.data = self._create_empty_board()

    def _create_empty_board(self): 
        """
        Create the board function
        """
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        pass

    def get_board(self):
        return self.data