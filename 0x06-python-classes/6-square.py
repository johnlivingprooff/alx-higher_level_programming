#!/usr/bin/python3
"""A group of functions that define a square class"""


class Square:
    """This Class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square

        Args:
            size (int): size of the Square (length of one side)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # define the area method
    def area(self):
        """returns the area of the square"""
        return self.size**2

    # printing the square with '#'
    def my_print(self):
        """prints the square with '#'"""
        if self.size == 0:
            print()
        i = 0
        for _ in range(self.position[1]):
            print()
        while i < self.size:
            for _ in range(self.position[0]):
                print(" ", end='')
            for j in range(self.size):
                print("#", end='')
            print()
            i += 1
