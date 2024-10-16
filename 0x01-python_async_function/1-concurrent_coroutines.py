#!/usr/bin/env python3
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create lost of tasks"""
    tasks = [wait_random(max_delay) for _ in range(n)]

    """Gather results"""
    tasks = asyncio.as_completed(tasks)
    delays = [await task for task in tasks]
    """Return the delays in ascending order using heap"""
    return delays
