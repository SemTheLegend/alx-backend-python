#!/usr/bin/env python3
"""
This module defines a function that measures the runtime

Of an asynchronous function.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns the total execution time for this function."""

    start = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start

    return total_time
