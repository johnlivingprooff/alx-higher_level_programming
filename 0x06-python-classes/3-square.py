#!/usr/bin/python3
"""A group of functions that define a square class"""
class Square:
    """This Class represents a square
    it is defined in ...
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # define the area method
    def area(self):
        return self.__size**2
