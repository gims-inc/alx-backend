#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class
    """

    def __init__(self):
        """initialise
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            pass
        self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key
        """
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
