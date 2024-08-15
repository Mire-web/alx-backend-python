#!/usr/bin/env python3
"""
Sum all element of a mixed type list of int and float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of all elements in the list """
    total = 0
    for x in mxd_lst:
        total = total + x
    return total
