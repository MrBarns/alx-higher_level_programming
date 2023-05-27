#!/usr/bin/python3
"""

Unittest for max_integer([..])

"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to define tests for the ``max_integer`` function"""

    def test_list_integer(self):
        """Test max_integer with list of ints argument"""

        self.assertEqual(max_integer([100, 8, 5, 7, 11]), 100)
        self.assertEqual(max_integer([11, 8, 5, 7, 100]), 100)
        self.assertEqual(max_integer([5, 8, 100, 7, 11]), 100)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5, 8, 100, 7, -11]), 100)
        self.assertEqual(max_integer([-52, -81, -100, -74, -10]), -10)
