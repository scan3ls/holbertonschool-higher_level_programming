#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
#"{:d}".format(x)
    for idx in range(len(matrix)):
        print(*matrix[idx], sep=' ')
