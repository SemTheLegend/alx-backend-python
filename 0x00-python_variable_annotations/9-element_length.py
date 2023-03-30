#!/usr/bin/env python3
"""This module returns a function that returns with appropriate types."""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the appropriate values."""

    return [(i, len(i)) for i in lst]
