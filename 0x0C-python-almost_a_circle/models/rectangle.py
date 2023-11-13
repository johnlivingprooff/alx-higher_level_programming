#!/usr/bin/python3
"""this module contains a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """this class defines a retangle"""

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantisation"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("\n")

        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print(self.print_symbol, end="")
            print()

    def __str__(self):
        msg = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return msg

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.__width = args[0]
            if len(args) > 1:
                self.__height = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) > 3:
                self.__y = args[3]
            if len(args) > 4:
                self.id = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        rect_dict = {"width": self.__width, "height": self.__height,
                     "x": self.__x, "y": self.__y, "id": self.id}
        return rect_dict
