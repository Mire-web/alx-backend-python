#!/usr/bin/env python3
"""
Async Coroutine that takes integer and returns random after delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    await asyncio.sleep(max_delay)
    result = random.uniform(0, max_delay + 1)
    return result
