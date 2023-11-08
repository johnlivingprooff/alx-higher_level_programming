#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """implement a recursive serialization"""
    if not isinstance(obj, object):
        return None
    def serialize(data):
        """a recursive approach to serialization"""
        # the main core of the function
        if isinstance(data, (int, str, bool)):
            return data
        # where the obj is a list
        elif isinstance(data, list):
            return [serialize(item) for item in data]
        # where obj is a dict
        elif isinstance(data, dict):
            return {str(key): serialize(item) for key, item in data.items()}
        elif isinstance(data, '__dict__'):
            return {str(key): serialize(item)
                    for key, item in data.__dict__.items()}
        else:
            return None
    return serialize(obj)
