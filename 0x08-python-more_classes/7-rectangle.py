#!/usr/bin/python3
"""
A class that defines a Rectangle
"""


class Rectangle:
    """The class represents a Rectangle

    Attributes:
        number_of_instances (int): the number of instances of the class
        print_symbol(str): the print symbol
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height * self.__width)

    def __str__(self):
        """returns the printable representation of Rectancle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        row = [str(self.print_symbol) * self.__width]
        return '\n'.join(row * self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
