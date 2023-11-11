#!/usr/bin/python3
"""This module contains the base Class for
Almost a Circle"""


class Base:
    """the base class for Almost
    a circle"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod    
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None:
            return "[]"
        str_rep = json.dumps(list_dictionaries)
        return str_rep
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dict)
                file.write(json_str)

    def from_json_string(json_string):
        import json
        if json_string is None:
            return "[]"
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_ins = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy_ins = cls(5)
        
        dummy_ins.update(**dictionary)
        return dummy_ins
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file"""
        import json

        filename = cls.__name__ + ".json"
        
        try:
            with open(filename, "r") as file:
                data = file.read()
                if not data:
                    return []
                
                list_dicts = cls.from_json_string(data)
                instances = [cls.create(**obj) for obj in list_dicts]
                return instances
        except FileNotFoundError:
            return []


