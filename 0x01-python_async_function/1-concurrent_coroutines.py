#!/usr/bin/env python3
"""
Run concurrent Coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return Sorteed list """
    async_list = [wait_random(max_delay) for _ in range(n)]
    sorted_list = [await task for task in asyncio.as_completed((async_list))]
    return sorted_list
