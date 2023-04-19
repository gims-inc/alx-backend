#!/usr/bin/python3
""" LRU  caching implimentation"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class

    Args:
        BaseCaching (class): Basic class for this class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache

        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if key and item:
            self.cache_data.update({key: item})
            lru_key = list(self.cache_data.keys())[0]

        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(lru_key)
            print('DISCARD: {}'.format(lru_key))

    def get(self, key):
        """Get an item by key

        Args:
            key ([type]): key to search into cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
