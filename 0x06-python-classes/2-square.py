#!/usr/bin/python3
"""Define square object with error messages

"""


class Square:
    """Square object.

    Attributes:
        size: size of the square.
    """

    def __init__(self, size=0):
        """makes a square"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
