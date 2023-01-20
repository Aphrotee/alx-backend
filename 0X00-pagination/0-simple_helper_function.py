#!/usr/env python3

"""
This module provides the function index_range
"""


def index_range(page, page_size):
    """
    Thsi function returns a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    if not isinstance(int, page) or not isinstance(int, page_size):
        return
    end = page * page_size
    start = end - page_size
    indexRange = (start, end)
    return indexRange