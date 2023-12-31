#!/usr/bin/python3
"""this module inherits a rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class defines a square
    based on Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str reps"""
        msg = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
        return msg

    @property
    def size(self):
        """gets width"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary"""
        sq_dict = {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
        return sq_dict
