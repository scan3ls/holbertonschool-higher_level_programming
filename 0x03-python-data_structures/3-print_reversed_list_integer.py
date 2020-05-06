#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    length = length * -1
    i = -1
    while i >= length:
        print(my_list[i])
        i = i - 1
