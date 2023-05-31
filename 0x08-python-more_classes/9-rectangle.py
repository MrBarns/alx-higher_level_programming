#!/usr/bin/python3
"""

Module that defines a rectangle

"""


class Rectangle:
    """Class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object

        Args:
            width (int, optional): width of rectangle object
            height (int, optional): height of rectangle object

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Function to calculate the area of a Rectangle object"""

        return self.width * self.height

    def perimeter(self):
        """Function to calculate the perimeter of a Rectangle object"""

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        """Function to depict object as string"""

        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height):
            for w in range(self.width):
                rectangle += "{}".format(self.print_symbol)

            if h != self.height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """Function to define official string representation of object"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Function defines deletion of an object"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Method to find biggest triangle"""

        try:
            if type(rect_1) != Rectangle:
                raise TypeError("rect_1 must be an instance of Rectangle")
            if type(rect_2) != Rectangle:
                raise TypeError("rect_2 must be an instance of Rectangle")
        except Exception as e:
            raise e
        else:
            return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create Rectangle object of equal width and height"""

        return Rectangle(size, size)
