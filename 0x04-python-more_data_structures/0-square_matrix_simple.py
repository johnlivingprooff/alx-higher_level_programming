#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Creates a new matrix, with similar dimensions as matrix
    new_matrix = [
            [0 for _ in range(len(matrix[0]))]
            for _ in range(len(matrix))
            ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
