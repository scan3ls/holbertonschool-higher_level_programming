#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    d = a_dictionary
    if key in d:
        del d[key]
    return d
