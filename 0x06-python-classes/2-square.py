#!/usr/bin/python3
class Square:
    """makes a square"""
    def __init__(self, size=0):
        try:
            if isinstance(size, int) is False:
                raise TypeError
            elif size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise
