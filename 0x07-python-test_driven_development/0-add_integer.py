#!/usr/bin/python3
"""

Module defines function for adding integers

"""


def add_integer(a, b=98):
    """Function adds 2 integers. Casts arguments to int

    Args:
        a (int): First parameter
        b (int, optional): The second parameter. Defaults to 98.

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a or b are not of type int or float

    """

    for key, val in {'a': a, 'b': b}.items():
        if type(val) != int and type(val) != float:
            raise TypeError(f"{key} must be an integer")

    return int(a) + int(b)
