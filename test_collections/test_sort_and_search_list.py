"""
Program name: test_sort_and_search_list.py
Author: Rachel Li
Last date modified: 06/19/2020

The purpose of this program is to test sort_and_search_list
"""
import unittest
import unittest.mock as mock
from fun_with_collections import sort_and_search_list as ssl

class TestList(unittest.TestCase):
    def test_search_list_found(self):
        self.assertEqual(ssl.search_list('peach'), 4)
    def test_search_list_not_found(self):
        with self.assertRaises(ValueError):
            ssl.search_list('chocolate')
    def test_sort_list(self):
        self.assertEqual(ssl.sort_list(),None)

if __name__ == '__main__':
    unittest.main()
