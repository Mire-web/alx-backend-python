#!/usr/bin/env python3
"""
Async Generator coroutine to generate random numbers
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """ Yield random numbers between 0 and 10 """
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
