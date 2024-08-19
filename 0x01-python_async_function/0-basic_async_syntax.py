#!/usr/bin/env python3
"""
Async Coroutine that takes integer and returns random after delay
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    result = uniform(0, max_delay + 1)
    await asyncio.sleep(max_delay)
    return result
