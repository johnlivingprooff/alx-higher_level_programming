#!/usr/bin/python3
"""A group of functions that define a square class"""


class Square:
    """This Class represents a square"""
    def __init__(self, size=0):
        """Initialize the Square

        Args:
            size (int): size of the Square (length of one side)
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # define the area method
    def area(self):
        """returns the area of the square"""
        return self.size**2

    # printing the square with '#'
    def my_print(self):
        """prints the square with '#'"""
        if self.size == 0:
            print()
        i, j = 0, 0
        while i < self.size:
            for j in range(self.size):
                print("#", end='')
            print()
            i += 1
