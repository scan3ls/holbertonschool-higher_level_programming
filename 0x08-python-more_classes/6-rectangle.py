#!/usr/bin/python3
"""Defines a Rectangle
"""


class Rectangle:
    """Creates a Rectangle

    Attributes:
        number_of_instances: rectangle counter
        print_symbol: rectangle vertex printing symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return area"""
        width = self.width
        height = self.height
        return width * height

    def perimeter(self):
        """Calculate and return perimeter"""
        width = self.width
        height = self.height

        if width == 0 or height == 0:
            return 0
        return 2 * (width + height)

    def __str__(self):
        """Prints visual rectangle"""
        symbol = str(type(self).print_symbol)
        width = self.width
        area = self.area()

        print(symbol)
        string = ""
        for i in range(area):
            string = string + symbol
            if (i + 1) % width == 0 and (i + 1) / area != 1:
                string = string + '\n'
        return str(string)

    def __repr__(self):
        """Return string representation of a rectangle"""
        width = self.width
        height = self.height

        string = "Rectangle({}, {})".format(width, height)
        return string
