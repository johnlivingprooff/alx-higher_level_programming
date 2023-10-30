#!/usr/bin/python3
"""
This module contains a function that
prints a square with the '#' character

"""


def print_square(size):
    """this function prints a square

    Args: size(int): the size of the square

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
