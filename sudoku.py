sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


class Board:
    """
    A Board class that contains Tile Classes
    """

    def __init__(self, board):
        self.board = [[Tile(board[row][col], col, row)
                       for col in range(len(board[0]))]
                      for row in range(len(board))]

        self.tiles = [tile for row in self.board for tile in row]

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
        return self.board[y][x]


    def test_tile(self, tile):
        row_tiles = (tile for tile in self.board[tile.y])
        col_tiles = (tile for row in self.board for tile in row[tile.x])
        box_x, box_y = tile.x//3, tile.y//3
        box_tiles = (self.board[y][x] for y in range(box_y * 3, box_y * 3 + 3) for x in range(box_x * 3, box_x * 3 + 3))

        for other_tile in row_tiles:
            if other_tile.value == tile.value and tile != other_tile:
                return False

        for other_tile in col_tiles:
            if other_tile.value == tile.value and tile != other_tile:
                return False

        for other_tile in box_tiles:
            if other_tile.value == tile.value and tile != other_tile:
                return False

        return True


class Tile:
    """
    A Tile Class that contains tile info (value, x_position, y_position)
    """

    def __init__(self, value, col, row):
        self.value = value

        self.x = col
        self.y = row

    def __str__(self):
        return f'(x:{self.x}, y:{self.y} | value: {self.value})'

    def __repr__(self):
        return f'Tile({self.value}, {self.x}, {self.y})'


def run():
    board = Board(sudoku)
    for tile in board.tiles:
        pass


if __name__ == "__main__":
    run()
