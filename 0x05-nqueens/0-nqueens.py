#!/usr/bin/python3
""" task """


import sys


def is_safe(board, row, col, N):
    """Check this row on the left side"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """ solve """
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0

    return False


def solve_nqueens(N):
    """ solve """
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return False

    for row in board:
        print(" ".join(str(x) for x in row))

    return True


def print_solutions(board, col, N):
    """ print """
    if col == N:
        print([[i, row.index(1)] for i, row in enumerate(board)])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            print_solutions(board, col + 1, N)
            board[i][col] = 0


def main():
    """ main """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    print_solutions(board, 0, N)


if __name__ == "__main__":
    main()
