# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    def test_right_triangle(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right')

    def test_equilateral_triangle(self): 
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles')

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(6, 7, 8), 'Scalene')

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle')

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(210, 100, 100), 'InvalidInput')
        self.assertEqual(classify_triangle(0, 1, 1), 'InvalidInput')
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidInput')
        self.assertEqual(classify_triangle(1.5, 1, 1), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()
