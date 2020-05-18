#!/usr/bin/python3
def safe_print_integer(value):
    test = isinstance(value, int)
    try:
        print("{:d}".format(value))
        return (True)
    except:
        return (False)
