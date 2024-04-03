#!/usr/bin/python3
"""
Module - 1-fifo_cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """

    def __init__(self):
        """
        Initializes the FIFOCache
        """
        super().__init__()
        self.order_list = []

    def put(self, key, item):
        """
        Adds items to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.order_list) == BaseCaching.MAX_ITEMS:
                first_key = self.order_list.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.order_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the item in cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
