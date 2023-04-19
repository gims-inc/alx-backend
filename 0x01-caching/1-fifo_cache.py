#!/usr/bin/python3
""" FIFO """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class
    """

    def __init__(self):
        """Initialise
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data.update({key: item})
            first_key_in = list(self.cache_data.keys())[0]
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(first_key_in)
            print('DISCARD: {}'.format(first_key_in))

    def get(self, key):
        """Get an item by key
        """
        if key or key in self.cache_data:
            return self.cache_data[key]
        return None
