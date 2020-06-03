#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Create and print pascal's triangle"""
    if n <= 0:
        return []

    triangle = []

    for height in range(0, n):
        triangle.append([1])
    if n == 1:
        return triangle

    for idx in range(1, n):
        triangle[idx].append(idx)
    if n == 2:
        return triangle

    for row in range(2, n):
        current_row = triangle[row]
        prev_row = triangle[row - 1]
        index = 2

        while index < len(prev_row):
            prev_2 = prev_row[index]
            prev_1 = prev_row[index - 1]
            index += 1
            current_row.append(prev_1 + prev_2)
        current_row.append(1)

    return triangle
