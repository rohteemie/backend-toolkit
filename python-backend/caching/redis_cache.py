import redis
from os import getenv

class RedisCache:
    """A cache manager using Redis."""
    def __init__(self):
        self.redis_host = getenv("REDIS_HOST", "localhost")
        self.redis_port = int(getenv("REDIS_PORT", 6379))
        self.redis_db = int(getenv("REDIS_DB", 0))
        self.client = redis.StrictRedis(host=self.redis_host, port=self.redis_port, db=self.redis_db)

    def set(self, key, value, ttl=None):
        """Set a key-value pair in the cache with optional TTL (Time-to-Live)."""
        try:
            self.client.set(key, value, ex=ttl)
        except redis.RedisError as e:
            print(f"Error setting cache key: {e}")

    def get(self, key):
        """Get the value for a given key."""
        try:
            return self.client.get(key)
        except redis.RedisError as e:
            print(f"Error retrieving cache key: {e}")
            return None

    def delete(self, key):
        """Delete a key from the cache."""
        try:
            self.client.delete(key)
        except redis.RedisError as e:
            print(f"Error deleting cache key: {e}")

    def clear(self):
        """Clear the entire cache."""
        try:
            self.client.flushdb()
        except redis.RedisError as e:
            print(f"Error clearing cache: {e}")
