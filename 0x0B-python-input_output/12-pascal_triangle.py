#!/usr/bin/python3
"""Technical interview preparation:
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triad = [[1]]

    for row in range(1, n):
        prev = triad[row - 1]
        new = [1]

        for i in range(1, row):
            element = prev[i - 1] + prev[i]
            new.append(element)

        new.append(1)
        triad.append(new)

    return triad
