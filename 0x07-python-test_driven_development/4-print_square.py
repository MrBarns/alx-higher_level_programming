#!/usr/bin/python3
"""

Module defines a function to print a square

"""


def print_square(size):
    """Function to print a square of specified size

    Args:
        size (int): Size of the square's sides. Must be positive integer

    Returns:
        Nothing

    Raises:
        ValueError: if size is less than 0
        TypeError: if size is not an integer

    """

    try:
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    except Exception as e:
        raise e
    else:
        y = size
        while y > 0:
            x = size
            while x > 0:
                print("#", end="")
                x -= 1
            print()
            y -= 1
