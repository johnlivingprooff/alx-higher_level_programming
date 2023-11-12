#!/usr/bin/python3
"""This module contains Test Cases for
models/rectangle.py"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """property evaluation"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        inst = Rectangle(4, 6)
        self.assertEqual(inst.width, 4)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            Rectangle(4.5, 6)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 6)

    def test_width_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 5)

    def test_height(self):
        inst = Rectangle(4, 6)
        self.assertEqual(inst.height, 6)

    def test_height_float(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 4.5)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(6, -5)

    def test_height_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(4, float('inf'))

    def test_x_int(self):
        inst = Rectangle(4, 6, 2, 2)
        self.assertEqual(inst.x, 2)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 4.5)

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -5)

    def test_x_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, float('inf'))

    def test_x_None(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, None)

    def test_y_int(self):
        inst = Rectangle(4, 6, 2, 2)
        self.assertEqual(inst.y, 2)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 4.5)
        
    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -5)

    def test_y_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, float('inf'))

    def test_y_None(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, None)

    def test_update_args(self):
        obj = Rectangle(10, 5, 4, 4, 2)
        obj.update()

        self.assertEqual("[Rectangle] (2) 4/4 - 10/5", str(obj))

    def test_update_kwargs(self):
        obj = Rectangle(10, 6)
        obj.update(width=5, id=4)

        self.assertEqual("[Rectangle] (4) 0/0 - 5/6", str(obj))

    def test_to_dictionary(self):
        obj = Rectangle(15, 45, 2, 2, 10)
        a_dict = obj.to_dictionary()

        self.assertEqual(a_dict, {"width":15, "height":45,
                                  "x":2, "y":2, "id":10})


if __name__ == "__main__":
    unittest.main()
