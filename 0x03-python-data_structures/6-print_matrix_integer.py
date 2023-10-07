#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i, a in enumerate(x):
            if i == len(x) - 1:
                print('{}'.format(a), end="")
            else:
                print('{}'.format(a), end=" ")
        print()
