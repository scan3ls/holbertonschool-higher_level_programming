#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    cpy = a_dictionary.copy()
    cpy_list = sorted(cpy.keys())
    for key in cpy_list:
        print("{}: {}".format(key, cpy[key]))
