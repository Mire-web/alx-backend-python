#!/usr/bin/env python3
"""
Comprehensively collect 10 random outputs from async_generator
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Return a comprehensive list of generated random numbers """
    return [i async for i in async_generator()]
