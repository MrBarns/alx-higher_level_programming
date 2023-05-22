#!/usr/bin/python3
"""Create Square class with controls for private and public attribute"""


class Square:
    """Defines class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Creates instance of type Square

        Args:
            size (int): length of Square object's sides
            position (tuple): tuple of 2 positive integers

        """

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: tuple of 2 positive integers"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position attribute"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Returns the area of a Square object"""

        return self.__size ** 2

    def my_print(self):
        """prints current square area with #"""

        x = self.__size
        if self.__size == 0:
            print()
            return

        for c in range(self.__position[1]):
            print()

        for x in range(self.__size):
            for b in range(self.__position[0]):
                print(" ", end="")

            for y in range(self.__size):
                print("#", end="")

            print()
