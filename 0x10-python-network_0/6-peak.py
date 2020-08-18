#!/usr/bin/python3
""" Peak finder """

def find_peak(list_of_integers):
    """ finder """

    if list_of_integers is None:
        return None
    if type(list_of_integers) is not list:
        return None
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    mid = int(length / 2)
    start = list_of_integers[mid]

    current = start
    max_right = find_peak(list_of_integers[mid:])
    max_left = find_peak(list_of_integers[:mid])

    if max_left is None or current is None or max_right is None:
        return None

    if max_left < current > max_right:
        return current
    elif current < max_left > max_right:
        return max_left
    else:
        return max_right
