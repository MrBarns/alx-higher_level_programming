#!/usr/bin/python3
"""Create Square class with controls for private attribute"""


class Square:
    """Defines class representing a square"""

    def __init__(self, size=0):
        """Creates instance of type Square

        Args:
            size (int): length of Square object's sides

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
