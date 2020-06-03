#!/usr/bin/python3
"""Read a file"""


def number_of_lines(filename=""):
    """Counts lines of a file"""
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count
