#!/usr/bin/env python3
""" Define asychroneous routine"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Generate a random delay between 0 and max_delay(10)"""
    delay_value = random.uniform(0, max_delay)
    """Await for the random delay"""
    await asyncio.sleep(delay_value)
    """Return delay value"""
    return delay_value
