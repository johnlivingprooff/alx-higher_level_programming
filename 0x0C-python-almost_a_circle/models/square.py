#!/usr/bin/python3
"""this module inherits a rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class defines a square
    based on Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        msg = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
        return msg

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
