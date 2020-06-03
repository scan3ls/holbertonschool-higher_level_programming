#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Prints contents of a file"""
    with open(filename) as f:
        output = f.read()
    print(output)
