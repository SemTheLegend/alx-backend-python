#!/usr/bin/env python3
"""
This module executes multiple coroutines at the same time with async.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    n must be an integer,
    max_delay must be an integer.
    Returns a list of float values in ascending order.
    """
    res = []
    for i in range(n):
        res.append(asyncio.create_task(task_wait_random(max_delay)))

    for i in range(0, len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                temp = res[i]
                res[i] = res[j]
                res[j] = temp
    return res
