#!/usr/bin/env python3
"""
    Test for access_nested map
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import requests
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
    Class to test get_json function
    """
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self,
                      test_url: str,
                      test_payload: dict,
                      mock_response) -> None:
        mock_response.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        #mock_response.assert_called_once_with(test_url)



if __name__ == '__main__':
    unittest.main()
