#!/usr/bin/python3
"""This module contains a function
that returns a new matrix
"""


def matrix_divided(matrix, div):
    """returns a new matrix
    Args:
        matrix: a list of lists
        div: the divisor"""
    new_matrix = []

    if not matrix:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    if not all(isinstance(row, list) and
               all(isinstance(val, (int, float))
                   for val in row) for row in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    coln = len(matrix[0])
    if any(len(row) != coln for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        rows = []
        for j in range(len(matrix[i])):
            result = matrix[i][j] / div
            if isinstance(result, float):
                result = round(result, 2)
            rows.append(result)
        new_matrix.append(rows)

    return new_matrix
