#!/usr/bin/env python3
"""
This module defines a function that takes a float as an argument

and returns a function that multiplies a float by that arg.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a float arg multiplied by float arg."""

    return lambda x: x * multiplier
