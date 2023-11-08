#!/usr/bin/python3
"""Contains a Student Class"""


class Student:
    """This defines the student class"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """filtering"""
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
        
