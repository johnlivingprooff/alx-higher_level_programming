#!/usr/bin/python3
"""This module contains Test Cases for
Project Almost a Circle"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """tests for base class"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_create(self):
        obj = Base()
        obj2 = Base(5)
        obj3 = Base(2)
        obj4 = Base(5.8)
        obj5 = Base(None)
        obj6 = Base(-9)

        self.assertEqual(obj.id, 11)
        self.assertEqual(obj2.id, 5)
        self.assertEqual(obj3.id, 2)
        self.assertEqual(obj4.id, 5.8)
        self.assertEqual(obj5.id, 12)
        self.assertEqual(obj6.id, -9)

    def test_to_json_string(self):
        j_str = Base.to_json_string(None)

        self.assertEqual(j_str, "[]")

    def test_from_json_string(self):
        j_str = Base.from_json_string(None)

        self.assertEqual(j_str, [])


class BaseTest_file(unittest.TestCase):
    """checks file operaion"""
    def test_save_load_file_rectangle(self):
        obj = Rectangle(4, 6)
        obj1 = Rectangle(10, 25)
        obj2 = Rectangle(15, 4)

        Rectangle.save_to_file([obj, obj1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertTrue(len(content), 52)
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

        Rectangle.save_to_file([obj1, obj2])
        instance = Rectangle.load_from_file()

        self.assertEqual(len(instance), 2)
        self.assertEqual(instance[0].id, 2)
        self.assertEqual(instance[1].id, 3)

    def test_empty_file_rectangle(self):
        Rectangle.save_to_file(None)
        instance = Rectangle.load_from_file()

        self.assertEqual(len(instance), 0)

    def test_save_load_file_square(self):
        obj = Square(6)
        obj1 = Square(25)
        obj2 = Square(15)

        Square.save_to_file([obj, obj1])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertTrue(len(content), 52)
        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

        Square.save_to_file([obj1, obj2])
        instance = Square.load_from_file()

        self.assertEqual(len(instance), 2)
        self.assertEqual(instance[0].id, 7)
        self.assertEqual(instance[1].id, 8)

    def test_empty_file_square(self):
        Square.save_to_file(None)
        instance = Square.load_from_file()

        self.assertEqual(len(instance), 0)


if __name__ == "__main__":
    unittest.main()
