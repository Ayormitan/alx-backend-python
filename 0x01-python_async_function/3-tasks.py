#!/usr/bin/env python3
import asyncio
from basic_async_sythax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
