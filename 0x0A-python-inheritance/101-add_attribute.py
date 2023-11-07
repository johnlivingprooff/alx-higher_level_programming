#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(_clas, id, val):
    """adds a new attribute where possible"""
    if hasattr(_clas, "__dict__"):
        setattr(_clas, id, val)
    else:
        raise TypeError("can't add new attribute")
