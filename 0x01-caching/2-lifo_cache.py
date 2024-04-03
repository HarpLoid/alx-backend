#!/usr/bin/python3
"""
Module - 2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """
        Initializes the LIFOCache
        """
        super().__init__()
        self.order_list = []

    def put(self, key, item):
        """
        Adds items to the cache
        """
        if key or item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order_list.remove(key)
                self.order_list.append(key)
                return

            if len(self.order_list) == BaseCaching.MAX_ITEMS:
                last_key = self.order_list.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.order_list.append(key)
            self.cache_data[key] = item

        else:
            pass

    def get(self, key):
        """
        returns the item in cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
