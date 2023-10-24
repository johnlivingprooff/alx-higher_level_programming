#!/usr/bin/python3
class Square:
    """This Class represents a square
    it defines the attributes and methods of a Square ...
    """
    def __init__(self, size=0):
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
        return self.size**2
