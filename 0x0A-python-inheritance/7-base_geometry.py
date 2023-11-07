#!/usr/bin/python3
"""module contains inherited classes"""


class BaseGeometry:
    """this class has  public method"""
    def __init__(self):
        pass

    def area(self):
        """should calculate the area or raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validated the integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
