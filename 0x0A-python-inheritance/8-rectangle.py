#!/usr/bin/python3
"""Doc"""


class BaseGeometry:
    """Empty"""
    def __init__(self):
        pass

    def area(self):
        """My B"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Quadurple check value"""
        for char in "Qaud":
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """make stuff"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
