#!/usr/bin/env python3
"""
Module to measure runtime of async comprehensions executed in parallel.
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total time it takes to run async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return end - start
