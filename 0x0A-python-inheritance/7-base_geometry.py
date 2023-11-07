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
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
