#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string:"""
import json


def from_json_string(my_str):
    obj = json.loads(my_str)
    # for k, v in obj.items():
    #     obj[k] = v
    return obj
