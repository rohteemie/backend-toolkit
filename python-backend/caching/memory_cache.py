import time
from threading import RLock


class MemoryCache:
    """A thread-safe in-memory cache manager."""

    def __init__(self):
        self.store = {}  # Dictionary to hold cached data
        self.lock = RLock()  # Ensure thread-safe access to the store

    def set(self, key, value, ttl=None):
        """
        Store a key-value pair in the cache with an optional Time-To-Live (TTL).
        :param key: The key to store.
        :param value: The value to store.
        :param ttl: Time-to-live in seconds (optional).
        """
        with self.lock:
            expiry_time = time.time() + ttl if ttl else None
            self.store[key] = {"value": value, "expiry": expiry_time}

    def get(self, key):
        """
        Retrieve a value from the cache by key.
        :param key: The key to retrieve.
        :return: The value if the key exists and is not expired, else None.
        """
        with self.lock:
            if key in self.store:
                entry = self.store[key]
                if entry["expiry"] is None or entry["expiry"] > time.time():
                    return entry["value"]
                else:
                    # Remove expired entry
                    del self.store[key]
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the cache.
        :param key: The key to delete.
        """
        with self.lock:
            if key in self.store:
                del self.store[key]

    def clear(self):
        """
        Clear all entries from the cache.
        """
        with self.lock:
            self.store.clear()

    def count(self):
        """
        Count the
