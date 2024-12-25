board = []

for i in range(8):
    board.append(["-" for _ in range(8)])


def print_board(board):
    for row in board:
        print(" ".join(row))

    print()


def can_place_queen(row, col, rows, cols, left_diangonals, right_diagonals):
    left_diagonal = row - col
    right_diagonal = row + col

    if row not in rows and col not in cols and left_diagonal not in left_diangonals and right_diagonal not in right_diagonals:
        return True
    else:
        return False

def place_queen(row, col, board, rows, cols, left_diangonals, right_diagonals):
    left_diagonal = row - col
    right_diagonal = row + col

    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diangonals.add(left_diagonal)
    right_diagonals.add(right_diagonal)

def remove_queen(row, col, board, rows, cols, left_diangonals, right_diagonals):
    left_diagonal = row - col
    right_diagonal = row + col

    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diangonals.remove(left_diagonal)
    right_diagonals.remove(right_diagonal)


def EightQueens(row, board, rows, cols, left_diangonals, right_diagonals):

    if row == 8:
        print_board(board)
        return 1


    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diangonals, right_diagonals):
            place_queen(row, col, board, rows, cols, left_diangonals, right_diagonals)
            EightQueens(row + 1, board, rows, cols, left_diangonals, right_diagonals)
            remove_queen(row, col, board, rows, cols, left_diangonals, right_diagonals)


EightQueens(0, board, set(), set(), set(), set())
