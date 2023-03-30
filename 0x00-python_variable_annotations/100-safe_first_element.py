#!/usr/bin/env python3 
"""This module has the correct duck-typed annotations."""



# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
