board = [
    [0,0,6,8,0,0,5,1,0],
    [0,0,5,0,4,6,0,9,0],
    [0,0,2,0,5,0,0,0,3],
    [5,0,8,0,0,2,0,0,0],
    [6,1,0,9,0,3,0,5,7],
    [0,0,0,4,0,0,8,0,9],
    [4,0,0,0,7,0,3,0,0],
    [0,5,0,2,3,0,9,0,0],
    [0,3,7,0,0,8,1,0,0]
]  # https://www.websudoku.com/?level=1&set_id=5108128121


def print_board(bp):  # bp=board parameter
    for i in range(len(bp)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")

        for j in range(len(bp[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bp[i][j])
            else:
                print(str(bp[i][j]) + " ", end="")


def find_empty(bp):
    for i in range(len(bp)):
        for j in range(len(bp[0])):
            if bp[i][j] == 0:
                return (i, j)    # i=row j=column

    return None


def valid(bp, num, pos):  # checking if number in box is valid
    # check row
    for i in range(len(bp[0])):
        if bp[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bp)):
        if bp[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # floor division by 3 results in this setup (x, y)
    # | 0, 0 | 1,0  | 2, 0 |
    # -   -   -   -   -   -
    # | 0, 1 | 1, 1 | 2, 1 |
    # -   -   -   -   -   -
    # | 0, 2 | 1, 2 | 2, 2 |

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bp[i][j] == num and (i, j) != pos:
                return False
    # made it to through all checks

    return True


def solve(bp):
    find = find_empty(bp)
    if not find:  # if empty cannot be found
        return True     # solved
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bp, i, (row, col)):
            bp[row][col] = i

            if solve(bp):  # recursive function
                return True

            bp[row][col] = 0

    return False


print("start: ")
print_board(board)
solve(board)
print("\n solved:")
print_board(board)