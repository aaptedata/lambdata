#!/c/Users/aapte/AppData/Local/Programs/Python/Python38/python
""" Unit testing the shape package """

import unittest
from shape import *

rect1 = Rectangle(5,7)
rect2 = Rectangle(8,4)
square1 = Square(6)
square2 = Square(2**0.5)
cube = Cube(6)

class ShapeTest(unittest.TestCase):

    def testCalc(self):
        self.assertEqual(rect1.perimeter(), rect2.perimeter())
        self.assertEqual(square2.area(), 2)
        self.assertEqual(cube.volume(), cube.surface_area())
        self.assertEqual(rect1.perimeter(), square1.perimeter())
        self.assertEqual(square1.area()-1, rect1.area())
        self.assertEqual(square1.area()-4, rect2.area())

if __name__ == "__main__": 
    unittest.main()