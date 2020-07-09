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
    # Get blank spaces
    if not get_blank(brd):
        return True
    else:
        row, col = get_blank(brd)

    for i in range(1, 10):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solver(brd):
                return True
            brd[row][col] = 0


def get_blank(brd):
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if brd[row][col] == 0:
                return row, col
    return None


def valid(brd, num, pos):
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
