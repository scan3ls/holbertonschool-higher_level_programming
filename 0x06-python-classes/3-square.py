#!/usr/bin/python3
"""Big boy docstring

"""


class Square:
    """makes a square"""
    def __init__(self, size=0):
        """init function"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """find area of the square"""
        return self.__size * self.__size
