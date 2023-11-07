#!/usr/bin/python3
"""module contains inherited classes"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this defines a rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """initialize the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
