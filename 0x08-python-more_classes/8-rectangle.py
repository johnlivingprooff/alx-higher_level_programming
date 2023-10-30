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
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ""
        txt = ""
        for i in range(self.__height):
            for j in range(self.__width):
                txt += type(self).print_symbol
            if i != self.__height - 1:
                txt += '\n'

        return txt

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        if area_1 < area_2:
            return rect_2
