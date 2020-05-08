#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for lst in matrix:
        thing = list(map(lambda x: x * x, lst))
        new_list.append(thing)
    return(new_list)
