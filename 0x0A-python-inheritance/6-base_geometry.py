#!/usr/bin/python3
"""module contains inherited classes"""


class BaseGeometry:
    """this class has a public method"""
    def area(self):
        """should calculate the area or raise Exception"""
        raise Exception("area() is not implemented")
