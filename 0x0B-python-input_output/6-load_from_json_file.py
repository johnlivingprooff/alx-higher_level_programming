#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """loads Obj form json file"""
    import json
    with open(filename, encoding="utf-8") as file:
        obj = json.load(file)
    return obj
