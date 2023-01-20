#!/usr/bin/env python3

"""
This module provides the class Server.
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    This function returns a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    if not isinstance(page, int) or not isinstance(page_size, int):
        return
    end = page * page_size
    start = end - page_size
    indexRange = (start, end)

    return indexRange


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This function takes two integer arguments page with
        default value 1 and page_size with default value 10
        and returns the page fetched
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexRange = index_range(page, page_size)
        data = self.dataset()
        response = []
        if indexRange[0] > len(data):
            pass
        elif indexRange[1] > len(data):
            response = data[indexRange[0]:]
        else:
            response = data[indexRange[0]:indexRange[1]]

        return response

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This method takes two integer arguments
        default value 1 and page_size with defualt value 10
        and returns a dictionary containing necessary information
        about the current page fetched
        """
        data = self.get_page(page, page_size)
        data_set = self.dataset()
        total_pages = len(data_set) // page_size
        if len(data_set) % page_size:
            total_pages += 1
        next_page = None
        prev_page = None
        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1
        page_info = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return page_info
