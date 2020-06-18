"""
Program name: test_basic_list_exception.py
Author: Rachel Li
Last date modified: 06/18/2020

The purpose of this program is to test basic_list_exception.py
"""
import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5,5,5])
    @patch('fun_with_collections.basic_list.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()
    def test_make_list_below_range(self):
        with self.assertRaises(ValueError): #when list is less than 1
            topic1.make_list()
    def test_make_list_above_range(self):
        with self.assertRaises(ValueError): #when list is greater than 50
            topic1.make_list()

if __name__=='__main__':
    unittest.main()
