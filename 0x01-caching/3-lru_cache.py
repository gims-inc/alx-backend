#!/usr/bin/python3
""" LRU  caching implimentation"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU cache class

    Args:
        BaseCaching (class): Basic class for this class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache

        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key

        Args:
            key ([type]): key to search into cache_data
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
