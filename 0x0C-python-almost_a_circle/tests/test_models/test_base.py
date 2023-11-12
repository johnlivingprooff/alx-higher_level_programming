#!/usr/bin/python3
"""This module contains Test Cases for
Project Almost a Circle"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests for base class"""
    def test_create(self):
        obj = Base()
        obj2 = Base(5)
        obj3 = Base()
        obj4 = Base(5.8)
        obj5 = Base(None)
        obj6 = Base(-9)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 5)
        self.assertEqual(obj3.id, 2)
        self.assertEqual(obj4.id, 5.8)
        self.assertEqual(obj5.id, 3)
        self.assertEqual(obj6.id, -9)

    def test_to_json_string(self):
        j_str = Base.to_json_string(None)

        self.assertEqual(j_str, "[]")

    def test_from_json_string(self):
        j_str = Base.from_json_string(None)

        self.assertEqual(j_str, [])


if __name__ == "__main__":
    unittest.main()
