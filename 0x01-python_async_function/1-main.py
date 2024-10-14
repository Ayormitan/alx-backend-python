#!/usr/bin/env python3

import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(3, 4)))
print(asyncio.run(wait_n(4, 8)))
print(asyncio.run(wait_n(10, 0)))
