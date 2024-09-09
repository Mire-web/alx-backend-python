#!/usr/bin/env python3
"""
Unit and Integration testing for utils class
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Any, Sequence
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing Accessed map class"""
    @parameterized.expand([
        ("test_1", {"a": 1}, ("a",), 1),
        ("test_2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test_3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name: Any,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_result: Any):
        """Testing Correct Map Accessing"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ("test_1", {}, ("a",)),
        ("test_2", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name: Any,
                                         nested_map: Mapping,
                                         path: Sequence):
        """Test exception raises"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
