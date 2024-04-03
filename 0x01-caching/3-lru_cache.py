#!/usr/bin/python3
"""
Module - 3-lru_cache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        """
        Initializes the LRUCache
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

            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lru_key = self.order_list.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.order_list.append(key)
            self.cache_data[key] = item

        else:
            pass

    def get(self, key):
        """
        returns the item in cache
        """
        if key in self.cache_data:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_data[key]
        return None
