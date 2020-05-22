#!/usr/bin/python3
"""
Contains single function for divided a matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix

        Args:
            matrix: matrix(list of lists) of numbers
            div: number to divide the matrix

        Returns:
            New matrix containing matrix values divided
            by div.
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_args = "matrix_divided() missing 1 required positional argument: 'div'"

    if matrix is None:
        raise TypeError(msg1)
    if div is None:
        raise TypeError(msg_args)
    if type(div) is not int:
        raise TypeError("div must be a number")

    length = len(matrix[0])

    for lst in matrix:
        if type(lst) is not list:
            raise TypeError(msg1)
        for i in lst:
            if type(i) is not int and type(i) is not float:
                raise TypeError(msg1)
        if len(lst) != length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: round(x / div, 2), new_matrix[i]))
    return new_matrix
