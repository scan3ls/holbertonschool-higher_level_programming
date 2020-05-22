#!/usr/bin/python3
"""Prints multi-line string with extra lines
"""


def text_indentation(text):
    """print extra lines after each occurance of ('.', '?', ':')

    Args:
        text: text to print with
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    start_of_line = True

    for char in text:

        if start_of_line is True and char is " ":
            start_of_line = False
            continue

        if char in special_chars:
            print(char)
            print()
            start_of_line = True
        else:
            print(char, end="")
