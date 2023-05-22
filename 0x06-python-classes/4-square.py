#!/usr/bin/python3
"""Create Square class with controls for private and public attribute"""


class Square:
    """Defines class representing a square"""

    def __init__(self, size=0):
        """Creates instance of type Square

        Args:
            size (int): length of Square object's sides

        """

        self.__size = size

    @property
    def size(self):
        """int: size of Square object's sides"""

        return self.__size

    @size.setter
    def size(self, value):
        """int: size of Square object's sides"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of a Square object"""

        return self.__size ** 2
