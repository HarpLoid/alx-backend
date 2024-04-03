#!/usr/bin/python3
"""
Module - 3-mru_cache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initializes the MRUCache
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
                self.order_list.remove(key)
                self.order_list.append(key)
                return

            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                mru_key = self.order_list.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.order_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the item in cache
        """
        if key in self.cache_data:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_data[key]
        return None
