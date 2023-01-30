#!/usr/bin/env python3
"""
    Test for access_nested map
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for utils.access_nested_map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)
 
    @parameterized.expand([
        ({}, ("a"), None),
        ({"a": 1}, {"a", "b"}, None),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: int) -> None:
        
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
