#!/usr/bin/python3
"""

Module that defines a rectangle

"""


class Rectangle:
    """Class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object

        Args:
            width (int, optional): width of rectangle object
            height (int, optional): height of rectangle object

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Function to retrieve Rectangle's width attribute"""

        return self.__width

    @property
    def height(self):
        """Function to retrieve Rectangle's height attribute"""

        return self.__height

    @width.setter
    def width(self, value):
        """Function to set width attribute of Rectangle object"""

        try:
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
        except Exception as e:
            raise e
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Function to set the height attribut of a Rectangle object"""

        try:
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
        except Exception as e:
            raise e
        else:
            self.__height = value
