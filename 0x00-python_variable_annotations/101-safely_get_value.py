#!/usr/bin/env python3
"""
Just annotate and submit
"""
from typing import Mapping, Any, Union, Generic, TypeVar
T = TypeVar('T')
myAny = Union[T, None]
anyY = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: myAny = None) -> anyY:
    """ get value from dictionary safely """
    if key in dct:
        return dct[key]
    else:
        return default
