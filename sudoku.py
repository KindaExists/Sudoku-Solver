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
        return self.board[y][x]

    def get_empty(self):
        for tile in self.tiles:
            if tile.value == 0:
                return tile

        return None

    def check_tile(self, in_tile):
        row_tiles = (tile for tile in self.board[in_tile.y])
        col_tiles = (row[in_tile.x] for row in self.board)
        box_x, box_y = in_tile.x//3, in_tile.y//3
        box_tiles = (self.board[y][x] for y in range(box_y * 3, box_y * 3 + 3) for x in range(box_x * 3, box_x * 3 + 3))

        for other_tile in row_tiles:
            if other_tile.value == in_tile.value and in_tile != other_tile:
                return False

        for other_tile in col_tiles:
            if other_tile.value == in_tile.value and in_tile != other_tile:
                return False

        for other_tile in box_tiles:
            if other_tile.value == in_tile.value and in_tile != other_tile:
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


def solve(board):
    cur_tile = board.get_empty()

    if not cur_tile:
        return True

    for value in range(1, 10):
        cur_tile.value = value
        if board.check_tile(cur_tile):
            if solve(board):
                return True
        cur_tile.value = 0

    return False


def run():
    board = Board(sudoku)

    if solve(board):
        print('Board has been solved, Final Board:')
        print(board)
    else:
        print('No solution can be found')
        print(board)


if __name__ == "__main__":
    run()
