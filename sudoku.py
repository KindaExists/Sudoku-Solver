class Board:
    """Contains Tile Classes in a 2D Array Grid

    Params:

    \---------------

            (list) board : A 9x9 2D List of integers used to set tile values

    Attributes

    \---------------

            (list) board : Where board is stored

    """

    def __init__(self, board):
        self.board = [[Tile(board[row][col], col, row)
                       for col in range(len(board[0]))]
                      for row in range(len(board))]

        self.tiles = [tile for row in self.board for tile in row]
        # Future Change(?): Can be switched to generator, might be cheaper

    def __str__(self):
        board_str = ''
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                board_str += '---------------------\n'

            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    board_str += '| '
                board_str += str(self.board[row][col].value) + ' '
            board_str += '\n'
        return board_str

    def get_tile(self, x, y):
        """Gets Tile object in the specified x, y position

        Params

        \---------------

                (int) x : The x Position of Tile

                (int) y : The y Position of Tile

        Raises

        \---------------

                IndexError : Index given is outside of range

        Returns

        \---------------

                Tile : A tile class, containing its value
        """
        return self.board[y][x]

    def get_empty(self):
        """Finds for the first empty tile in Board

        Returns

        \---------------

                Tile : First occurance of a tile with a value of 0

                None : If no tiles are empty
        """

        for tile in self.tiles:
            if tile.value == 0:
                return tile

        return None

    def check_tile(self, test_tile):
        """Checks if the given Tile object is valid

        Params

        \---------------

                (tile) test tile : The tile to be tested for validity

        Returns

        \---------------

                Bool : Depends on whether the tile is valid or not
        """

        row_tiles = (tile for tile in self.board[test_tile.y])
        col_tiles = (row[test_tile.x] for row in self.board)
        box_x, box_y = test_tile.x//3, test_tile.y//3
        box_tiles = (self.board[y][x] for y in range(box_y * 3, box_y * 3 + 3) for x in range(box_x * 3, box_x * 3 + 3))

        for other_tile in row_tiles:
            if other_tile.value == test_tile.value and test_tile != other_tile:
                return False

        for other_tile in col_tiles:
            if other_tile.value == test_tile.value and test_tile != other_tile:
                return False

        for other_tile in box_tiles:
            if other_tile.value == test_tile.value and test_tile != other_tile:
                return False

        return True


class Tile:
    """A Tile Class that contains tile info

    Params

    \---------------

            (int) value : Used to set the value of the Tile

            (int) col : Used to set the x position of the Tile

            (int) row : Used to set the y position of the Tile

    Attributes

    \---------------

            (int) value : Where value is stored

            (int) x : Where col is stored

            (int) y : Where row is stored

    """

    def __init__(self, value, col, row):
        self.value = value

        self.x = col
        self.y = row

    def __str__(self):
        return f'(x:{self.x}, y:{self.y} | value: {self.value})'

    def __repr__(self):
        return f'Tile({self.value}, {self.x}, {self.y})'


def fill(board):
    """Fills/Solves a sudoku board

    Params

    \---------------

            (Board) board : The sudoku board to be solved

    Returns

    \---------------

            Bool : Depends on success of solving, Returns False if Failure
    """
    empty_tile = board.get_empty()

    if not empty_tile:
        return True

    for value in range(1, 10):
        empty_tile.value = value
        if board.check_tile(empty_tile):
            if fill(board):
                return True
        empty_tile.value = 0

    return False