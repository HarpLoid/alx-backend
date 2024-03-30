#!/usr/bin/env python3
"""
Module simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing
    a start index and an end index
    corresponding to the range of indexes
    to return in a list for
    those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page data
        """
        assert isinstance(page_size, int) and isinstance(page, int) and page > 0 and page_size > 0
        if page > len(self.dataset()):
            return []
        idx_range = index_range(page, page_size)
        return self.__dataset[idx_range[0]:idx_range[1]]
