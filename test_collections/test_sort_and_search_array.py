"""
Program name: test_sort_and_search_array.py
Author: Rachel Li
Last date modified: 06/21/2020

The purpose of this program is to test sort_and_search_array.py
"""
import unittest
import unittest.mock as mock
from fun_with_collections import sort_and_search_array as ssa

class TestArray(unittest.TestCase):
    def test_search_array_found(self):
        self.assertEqual(ssa.search_array(5.9), 4)
    def test_search_array_not_found(self):
        with self.assertRaises(ValueError):
            ssa.search_array(69)
    def test_sort_array(self):
        self.assertEqual(ssa.sort_array(), None)

if __name__ == '__main__':
    unittest.main()
