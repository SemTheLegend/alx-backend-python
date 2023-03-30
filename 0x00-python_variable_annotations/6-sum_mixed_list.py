#!/usr/bin/env python3
"""
This module defines a function that takes a list of -

Mixed integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of args in the list."""

    sum = 0
    for num in mxd_list:
        sum += num

    return sum
