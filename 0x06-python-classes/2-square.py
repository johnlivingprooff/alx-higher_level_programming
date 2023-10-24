#!/usr/bin/python3
"""A group of functions that define a square class"""


class Square:
    """This Class represents a square"""
    def __init__(self, size=0):
        """Initialize the Square

        Args:
            size (int): size of the Square (length of one side)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
