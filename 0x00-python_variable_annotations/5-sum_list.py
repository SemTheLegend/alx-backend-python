#!/usr/bin/env python3
"""
This module defines a function that takes a list.

And returns the sum of the arguments.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of args of the list."""

    sum = 0
    for num in input_list:
        sum += num

    return sum
