#!/usr/bin/env python3
"""
Just annotate and return
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuples """
    return [(i, len(i)) for i in lst]
