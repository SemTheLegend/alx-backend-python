#!/usr/bin/env python3
"""
Module defines a coroutine that takes no arguments.
"""

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """
    yields a random number between 0 and 10.
    """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
