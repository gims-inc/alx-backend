#!/usr/bin/python3
""" LIFO """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class
    """

    def __init__(self):
        """Initialise
        """
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """Add an item in the cache
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
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
