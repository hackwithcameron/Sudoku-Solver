import board
from board import print_brd

test_board = board.test_board
board = board.board


def solver(brd):
    """
    Main solver function for Sudoku board.

    :param brd: Board to be solved
    :return: Solved Sudoku board
    """
    if not get_blank(brd):      # Finds blank spaces
        return True
    else:
        row, col = get_blank(brd)   # Unpacking return from get_blank()

    for i in range(1, 10):
        if valid(brd, i, (row, col)):   # Check to see if guess is valid
            brd[row][col] = i

            if solver(brd):
                return True
            brd[row][col] = 0


def get_blank(brd):
    """
    Finds first blank space on board.

    :param brd: Board to be solved.
    :return: Specific location of blank space on board.
    """
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if brd[row][col] == 0:
                return row, col
    return None


def valid(brd, num, pos):
    """
    Checks to see if guessed number is allowed in blank position.
    :param brd: Board
    :param num: Number guessed
    :param pos: Position on board for num
    :return: True if number is allowed. False if number already exists in row, col, or 3x3 box.
    """
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False
    # Check col
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False
    return True


print_brd(board)
solver(board)
print("\n -------------------------- \n")
print_brd(board)
