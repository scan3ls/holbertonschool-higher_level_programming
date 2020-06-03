#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """Writes text to a file"""

    with open(filename, 'a') as f:
        count = f.write(text)
    return count
