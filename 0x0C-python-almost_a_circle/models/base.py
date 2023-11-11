#!/usr/bin/python3
"""This module contains the base Class for
Almost a Circle"""


class Base:
    """the base class for Almost
    a circle"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
