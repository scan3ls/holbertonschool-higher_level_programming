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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
