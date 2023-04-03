#!/usr/bin/env python3
"""
This module defines a normal function `task_await_n`.

That is nearly identical to the imported function `wait_n`.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of float values in ascending order.
    """

    res = []
    for i in range(n):
        task = task_wait_random(max_delay)
        await task
        res.append(task)

    for i in range(0, len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
    return res
