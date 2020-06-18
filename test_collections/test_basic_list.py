"""
Program name: test_basic_list.py
Author: Rachel Li
Last date modified: 06/18/2020

The purpose of this program is to test basic_list.py
"""
import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5,5,5])

if __name__=='__main__':
    unittest.main()
