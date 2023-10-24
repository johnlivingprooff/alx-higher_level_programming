#!/usr/bin/python3
"""A group of functions that define a square class"""


class Square:
    """This Class represents a square"""
    def __init__(self, size):
        """Initialize the Square

        Args:
            size (int): size of the Square (length of one side)
        """
        self.__size = size
