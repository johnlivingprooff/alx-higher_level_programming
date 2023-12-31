#!/usr/bin/python3
"""module contains inherited classes"""


class BaseGeometry:
    """this class has a public method area"""

    def area(self):
        """should calculate the area or raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validated the integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
