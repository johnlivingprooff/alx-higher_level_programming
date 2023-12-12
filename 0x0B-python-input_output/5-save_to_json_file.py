#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation:"""


def save_to_json_file(my_obj, filename):
    """writes Object to text file"""
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
