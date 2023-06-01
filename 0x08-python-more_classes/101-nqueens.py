#!/usr/bin/python3
"""

Module defines a script that solves an N queens puzzle

"""


import sys


def no_clash(solution, x, y):
    """Function to check if a position on a board clashes with
    existing queens

    Args:
        solution (list): positions of existing queens on the board
        x (int): row coordinate of current position
        y (int): column coordinate of current position

    Returns:
        True or False (bool): to indicate a clash of queens

    """

    for square in solution:
        if square[0] == x or square[1] == y:
            return False
        if abs(square[0] - x) == abs(square[1] - y):
            return False

    return True


def nrecurs(N, solution, row):
    """Function to recursively check for solution to nqueens problem

    Args:
        N (int): number equal to 4 or greater. Represents the size of the board
        solution (list): list of solution found by function
        row (int): number denoting current board row in iteration

    Returns:
        True (bool): if viable solution is bound. False otherwise

    """

    if row == N:
        print("{}".format(solution))
        return

    for col in range(N):
        if no_clash(solution, row, col):
            solution.append([row, col])
            nrecurs(N, solution, row + 1)

            solution.pop()


def main(N):
    """Starter function for the 101-nqueens module

    Args:
        N (int): integer greater than or equal to 4. Denotes size of board

    """

    solution = []

    nrecurs(N, solution, 0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    main(N)
