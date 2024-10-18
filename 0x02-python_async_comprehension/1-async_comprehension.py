#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers using an async
comprehension over async_generator, then returns the 10 random numbers.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from an async generator function.
    Returns:
        List[float]: A list of 10 random float numbers.
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
