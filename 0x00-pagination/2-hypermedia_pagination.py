#!/usr/bin/env python3
"""Hypermedia pagination"""

import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Gets start index and end index

        Args:
            page (int): number of page
            page_size (int): size of page
        Returns:
            Tuple[int, int]: (start index, end index)
        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page
        Args:
            page (int, optional): number of page. Default eq 1.
            page_size (int, optional): number of row in page. Defaults eq 10.
        Returns:
            List[List]: List of dataset rows by range
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data_set = self.dataset()
        start, end = self.index_range(page, page_size)

        if end > len(data_set):
            return []
        return [data_set[start:end]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """gets hypermedia
        Args:
            page (int, optional): number of page. Defaults to 1.
            page_size (int, optional): number of row in page. Defaults to 10.
        Returns:
            Dict[ str, int]HATEOAS
        """
        totalPages = math.ceil(len(self.dataset()) / page_size)

        if page < 1:
            previousPage = None
        else:
            previousPage = page - 1

        if page >= totalPages:
            nextPage = None
        else:
            nextPage = page + 1

        hypermedia = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': nextPage,
            'prev_page': previousPage,
            'total_pages': totalPages
            }

        return hypermedia
