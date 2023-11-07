#!/usr/bin/python3
"""the function module"""


def inherits_from(obj, a_class):
    """returns true if obj inherits from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
