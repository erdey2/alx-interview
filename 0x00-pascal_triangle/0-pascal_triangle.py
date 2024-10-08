#!/usr/bin/python3
""" this module provide functionalities for pascal_triangle """


def pascal_triangle(n):
    """ pascal triangle function """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with 1

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
