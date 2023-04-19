#!/usr/bin/python3
""" LIFO caching implimentation"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class

    Args:
        BaseCaching (class): Basic class for this class
    """

    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Add an item in the cache

        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            last_key_in = self.__keys.pop()
            self.cache_data.pop(last_key_in)
            print('DISCARD: {}'.format(last_key_in))
        if key and item:
            self.cache_data.update({key: item})
            self.__keys.append(key)

    def get(self, key):
        """Get an item by key

        Args:
            key ([type]): key to search into cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
