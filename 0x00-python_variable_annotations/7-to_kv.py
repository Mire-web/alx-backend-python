#!/usr/bin/env python3
"""
Return a tuple containing str and squared int or float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """ Store result from parameter in a tuple """
    return (k, float(v) ** 2)
