#!/usr/bin/python3
"""

Module defines function to divide a matrix of ints and floats


"""


def matrix_divided(matrix, div):
    """ Function divides a matrix by an int of float.

    Args:
        matrix (list): first parameter. Matrix must contain only values of type
                       int and float
        div (int, float): second parameter.

    Returns:
        A matrix of numbers divided by div to two decimal places

    Raises:
        TypeError: if matrix is not a list of lists, if rows in matrix are not
                   of the same size and if div is not a integer/float
        ZeroDivisionError: if div is equal to 0

    """

    try:
        if type(matrix) != list or len(matrix) == 0:
            raise TypeError
        for x in matrix:
            if type(x) != list:
                raise TypeError
            for y in x:
                if type(y) != int and type(y) != float:
                    raise TypeError
    except TypeError:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    for x in matrix:
        if len(x) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for element in matrix:
        temp = []
        for num in element:
            temp.append(round(num / div, 2))
        new.append(temp)

    return new
