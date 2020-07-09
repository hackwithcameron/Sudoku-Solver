board = [
    [8, 0, 0, 4, 7, 0, 5, 0, 3],
    [0, 3, 6, 9, 8, 2, 1, 4, 0],
    [0, 0, 4, 0, 3, 5, 0, 8, 6],
    [6, 4, 8, 0, 0, 3, 0, 0, 9],
    [0, 0, 0, 2, 0, 0, 0, 0, 5],
    [3, 0, 5, 7, 0, 4, 0, 1, 0],
    [2, 0, 0, 8, 5, 1, 9, 7, 4],
    [0, 0, 0, 0, 0, 0, 0, 6, 1],
    [1, 8, 9, 6, 0, 7, 3, 5, 2]
]

test_board = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 3, 1]
]


def print_brd(brd):
    for row in range(len(brd)):
        if row % 3 == 0 and row != 0:
            print(" - - - - - - - - - - - - - - ")
        for num in range(len(brd[0])):
            if num % 3 == 0 and num != 0:
                print("|", end=" ")
            if num == 8:
                print(brd[row][num])
            else:
                print(str(brd[row][num]) + " ", end=" ")
