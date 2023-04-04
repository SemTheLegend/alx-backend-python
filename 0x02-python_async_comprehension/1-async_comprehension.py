#!/usr/bin/env python3
"""
Module defines a async comprehension function.
"""

import asyncio
from typing import Iterator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    """
    Returns 10 random numbers.
    """

    return [i async for i in async_generator()]
