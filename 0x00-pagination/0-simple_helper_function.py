#!/usr/bin/env python3
"""Function that takes two integer arguments page and page_size.
The function should return a tuple of size two containing
a start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Gets start index and end index
        Args:
            page (int): number of page
            page_size (int): size of page
        Returns:
            Tuple[int, int]: (start index, end index)
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
