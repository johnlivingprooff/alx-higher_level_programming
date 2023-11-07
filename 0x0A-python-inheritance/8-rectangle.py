#!/usr/bin/python3
"""module contains inherited classes"""


class BaseGeometry:
    """Class defines the base geometary"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """this defines a rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """initialize the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
