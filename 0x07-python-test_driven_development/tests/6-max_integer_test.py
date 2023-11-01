#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        Test cases for max_integer
    """

    def test_def(self):
        """Test case for normal use"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float(self):
        """Test case with float"""

        self.assertEqual(max_integer([1, 2, 3.7]), 3.7)

    def test_none(self):
        """tests empty input"""
        self.assertEqual(max_integer(), None)

    def test_non_int(self):
        """tests with non-int input"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])
    
    def test_neg_pos(self):
        """tests composed input"""
        self.assertEqual(max_integer([1, -4, -5, 5, 3]), 5)
    
    def test_neg(self):
        """tests negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

if __name__ == "__main__":
    unittest.main()
