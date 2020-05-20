#!/usr/bin/python3
"""Big boy docstring

"""


class Square:
    """makes a square"""
    def __init__(self, size=0):
        """init function"""
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

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """find area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print square with #"""
        size = self.__size

        if size == 0:
            print()
        for y in range(size):
            for x in range(size):
                print("#", end="")
            print()
