#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    t = ()

    for i in range(length):
        l = list(t)
        if my_list[i] % 2 == 0:
            l.append(True)
        else:
            l.append(False)
        t = tuple(l)

    return (t)
