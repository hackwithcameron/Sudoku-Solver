import board

test_board = board.test_board
board = board.board


def solver(brd):
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
    return True


for rows in test_board:
    print(rows)
solver(test_board)
for rows in test_board:
    print(rows)
