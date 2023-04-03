#!/usr/bin/env python3
"""
This module executes multiple coroutines at the same time with async.
"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n must be an integer,
    max_delay must be an integer.

    Returns a list of float values in ascending order.
    """
    res = []
    for i in range(n):
        res.append(await wait_random(max_delay))

    for i in range(0, len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
    return res
