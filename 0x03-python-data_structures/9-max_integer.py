#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    biggest = 0
    if length == 0:
        return (None)
    for i in range(length):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return (biggest)
