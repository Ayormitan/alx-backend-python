#!/usr/bin/env python3
import asyncio
from basic_async_syntax import wait_random

async def wait_n(n, max_delay) -> list:
    delays = []
    # Create lost of tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    #Gtaher results
    for delay in await asyncio.gather(*tasks):
        delays.append(delay)
    # Return the delays in ascending order using heapq
    return sorted(delays)
