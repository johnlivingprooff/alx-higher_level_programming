#!/usr/bin/python3
"""This module contains the base Class for
Almost a Circle"""
import turtle


class Base:
    """the base class for Almost
    a circle"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instantisation"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """from dict to json_string"""
        import json
        if list_dictionaries is None:
            return "[]"
        str_rep = json.dumps(list_dictionaries)
        return str_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """saves instances to a json file"""
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dict)
                file.write(json_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of objs to CSV"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            attrs = [attr for attr in vars(cls)
                     if not callable(getattr(cls, attr))
                     and not attr.startswith("__")]
        elif cls.__name__ == "Square":
            attrs = ('id', 'size', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("")
            else:
                for obj in list_objs:
                    csv_val = [str(getattr(obj, attr)) for attr in attrs]
                    file.write(",".join(csv_val))
                    file.write("\n")

    def from_json_string(json_string):
        """returns a loaded json str"""
        import json
        if json_string is None:
            return []
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

    @classmethod
    def load_from_file_csv(cls):
        """csv resolved"""
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                if not content:
                    return []

                list_objs = []
                header = None
            for row in content.split("\n"):
                if not header:
                    header = row.split(",")
                    continue

                args = row.split(",")
                obj_dict = {header[i]: int(args[i])
                            for i in range(len(header))}
                obj = cls(**obj_dict)
                list_objs.append(obj)

            return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws a shape"""
        shape = turtle.Turtle()

        for rect in list_rectangles:
            shape.pencolor("Blue")
            shape.width(5)
            shape.penup()
            shape.goto(rect.x, rect.y)
            shape.pendown()
            for _ in range(2):
                shape.forward(rect.width)
                shape.right(90)
                shape.forward(rect.height)
                shape.right(90)

        for sqr in list_squares:
            shape.pencolor("orange")
            shape.penup()
            shape.goto(sqr.x, sqr.y)
            shape.pendown()
            for _ in range(4):
                shape.forward(sqr.size)
                shape.right(90)

        shape.hideturtle()
