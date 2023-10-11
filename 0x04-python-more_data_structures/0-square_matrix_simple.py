#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Creates a new matrix, with similar dimensions as matrix
    new_matrix = [[0 for _ in range(len(matrix[]))] \
            for _ in range(len(martix))]
    new_matrix = [[x**2 for x in row] for x in matrix]

    return new_matrix
