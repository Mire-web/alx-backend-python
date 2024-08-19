#!/usr/bin/env python3
"""
Async Coroutine that takes integer and returns random after delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
