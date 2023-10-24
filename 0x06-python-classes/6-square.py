#!/usr/bin/python3
"""A group of functions that define a square class"""
class Square:
    """This Class represents a square
    it defines the attributes and methods of a Square ...
    """
    def __init__(self, size=0, position=(0, 0)):
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

    # define the area method
    def area(self):
        return self.size**2

    # printing the square with '#'
    def my_print(self):
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
