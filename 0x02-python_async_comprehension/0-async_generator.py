#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers using an async
comprehension over async_generator, then returns the 10 random numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that yields a random number between 0 and 10, ten times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
