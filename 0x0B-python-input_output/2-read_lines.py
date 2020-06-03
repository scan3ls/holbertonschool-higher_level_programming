#!/usr/bin/python3
"""Read a file"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a file"""

    output = ""

    with open(filename) as f:

        if nb_lines <= 0:
            output = f.read()

        line_counter = 0
        for line in f:
            if line_counter == nb_lines:
                break
            output += line
            line_counter += 1

        print(output)
