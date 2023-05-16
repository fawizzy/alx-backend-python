#!/usr/bin/env python3
"""
test utils
"""
import unittest
from unittest.mock import patch, Mock
from typing import Mapping, Sequence
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test sccess_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": 1}, ("b",), KeyError),
        ({"a": {"b": 2}}, ("b",), KeyError),
        ({"a": {"b": 2}}, ("b", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected: int) -> None:
        """test access nested map exception"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """
    class TestGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url: str, payload: dict, mock_get):
        """
        test get json
        """
        response = Mock()
        response.json.return_value = payload
        mock_get.return_value = response
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize
    """
    def test_memoize(self):
        """test memoize"""
        class TestClass:

            def a_method(self):
                """
                a sample method
                """
                return 42

            @memoize
            def a_property(self):
                """
                a sample property
                """
                return self.a_method()

        @patch('TestClass.a_method')
        def test_memoize(self, mock_a_method):
            """Mock the a_method"""
            mock_a_method.return_value = 42

            """Create an instance of TestClass"""
            instance = self.TestClass()

            # Call a_property twice
            result1 = instance.a_property()
            result2 = instance.a_property()

            # Assert that a_method was called once
            mock_a_method.assert_called_once()

            # Assert that the results are equal
            self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
