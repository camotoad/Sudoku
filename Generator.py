from random import *
from Solver import solve, valid, print_board
import copy
import sys
sys.setrecursionlimit(9999)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def clearboard():
    for i in range(0, 8):
        for j in range(0, 8):
            board[i][j].value = 0


def generate():
    rand = randint(15, 26)
    # print(rand)
    for i in range(rand):
        # seed(i * rand)
        row = randint(0, 8)
        col = randint(0, 8)
        value = randint(1, 9)

        # print('row: %r\n col: %r\nvalue:%r' % (row, col, value))
        # print_board(board)
        if valid(board, value, (row, col)):
            board[row][col] = value
        else:
            rand += 1
    for i in range(0, 8):   # validates the current value so recursion function doesn't hang
        for j in range(0, 8):
            if board[i][j] != 0:
                if valid(board, board[i][j], (i, j)):
                    pass
                    # print(self.model[i][j])
                else:
                    generate()
    temp = copy.deepcopy(board)
    print_board(temp)
    with recursionlimit(500):
        if solve(board):
            return temp
        else:
            clearboard()
            generate()


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


# print_board(generate())