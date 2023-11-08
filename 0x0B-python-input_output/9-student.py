#!/usr/bin/python3
"""Contains a Student Class"""


class Student:
    """This defines the student class"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """works similar to class_to_json"""
        if not isinstance(self, object):
            return None

        def serialize(data):
            """a recursive approach to serialization"""
            if isinstance(data, (int, str, bool)):
                return data

            elif isinstance(data, list):
                return [serialize(item) for item in data]

            elif isinstance(data, dict):
                return {str(key): serialize(item)
                        for key, item in data.items()}

            elif hasattr(data, '__dict__'):
                return {str(key): serialize(item)
                        for key, item in data.__dict__.items()}
            else:
                return None

        return serialize(self)
