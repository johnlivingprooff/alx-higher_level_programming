#!/usr/bin/python3
"""This module contains Test Cases for
models/rectangle.py"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """property evaluation"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size(self):
        inst = Square(6)
        self.assertEqual(inst.size, 6)

    def test_size_float(self):
        with self.assertRaises(TypeError):
            Square(4.5)

    def test_sizeIs_neg(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size_inf(self):
        with self.assertRaises(TypeError):
            Square(float('inf'))

    def test_size_None(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_x_int(self):
        inst = Square(6, 2, 2)
        self.assertEqual(inst.x, 2)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            Square(5, 4.5)

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            Square(5, -5)

    def test_x_inf(self):
        with self.assertRaises(TypeError):
            Square(5, float('inf'))

    def test_x_None(self):
        with self.assertRaises(TypeError):
            Square(5, None)

    def test_y_int(self):
        inst = Square(4, 2, 2)
        self.assertEqual(inst.y, 2)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            Square(5, 4.5)
        
    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, -5)

    def test_y_inf(self):
        with self.assertRaises(TypeError):
            Square(5, float('inf'))

    def test_y_None(self):
        with self.assertRaises(TypeError):
            Square(5, None)

    def test_update_args(self):
        obj = Square(5, 4, 5, 10)
        obj.update()

        self.assertEqual("[Square] (10) 4/5 - 5", str(obj))

    def test_update_kwargs(self):
        obj = Square(10)
        obj.update(size=5, id=4)

        self.assertEqual("[Square] (4) 0/0 - 5", str(obj))

    def test_to_dictionary(self):
        obj = Square(15, 2, 2, 10)
        a_dict = obj.to_dictionary()

        self.assertEqual(a_dict, {"size":15, "x":2, "y":2, "id":10})


if __name__ == "__main__":
    unittest.main()
