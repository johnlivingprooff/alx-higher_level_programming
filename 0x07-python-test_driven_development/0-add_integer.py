#!/usr/bin/python3
"""This add_integer module
    contains a function that returns
    the sum of two integers

"""


def add_integer(a, b=98):
    """Returns the sum of two integers
    Args: a (int): integer
          b (int): integer"""

    if isinstance(a, float):
        """if a is a float"""
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
