#!/usr/bin/env python3
"""
This module defines a function that takes a float as an argumrnt

and returns a function that multiplies a float by that arg.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a float arg multiplied by float arg."""

    def func_callable(multiplier):
        """Callable function."""

        return multiplier * multiplier

    return func_callable
