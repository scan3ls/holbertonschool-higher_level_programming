#!/usr/bin/python3
"""Write a file"""


def append_write(filename="", text=""):
    """Append test to a file
    
    Attributes:
        filename: name of file
        text: text to append to filename

    Return:
        count of characters wrote
    """

    with open(filename, 'a') as f:
        count = f.write(text)
    return count
