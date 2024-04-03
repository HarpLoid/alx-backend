#!/usr/bin/python3
"""
Module 0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class
    """

    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()

    def put(self, key, item):
        """
        puts an item into the cache
        with the key
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item

    def get(self, key):
        """
        returns the item in cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
