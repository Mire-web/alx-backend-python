#!/usr/bin/env python3
"""
Just annotate and submit
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first item on list safely """
    if lst:
        return lst[0]
    else:
        return None
