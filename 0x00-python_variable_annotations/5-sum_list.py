#!/usr/bin/env python3
"""
Returns sum of floating numbers in a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return sum of all floats in the list """
    total = 0
    for x in input_list:
        total = total + x
    return total
