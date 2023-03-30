#!/usr/bin/env python3
"""
This module defines a function that takes a string,

and an int or float as args and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of the passed args."""

    return(k, v ** 2)
