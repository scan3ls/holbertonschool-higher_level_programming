#!/usr/bin/python3
"""prints a square with '#'
"""


def print_square(size):
    """prints a square

    Args:
        size: size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        print('#' * size)
