import redis
import json
from datetime import timedelta

class RedisClient:
    """Handles Redis caching operations."""

    def __init__(self, host="localhost", port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def set(self, key, value, expiry_seconds=None):
        """
        Set a key-value pair in Redis.

        Args:
            key (str): Redis key.
            value (any): Value to store (serialized to JSON).
            expiry_seconds (int, optional): Time to live for the key in seconds.
        """
        value = json.dumps(value)
        if expiry_seconds:
            self.client.setex(key, timedelta(seconds=expiry_seconds), value)
        else:
            self.client.set(key, value)

    def get(self, key):
        """
        Retrieve a value by key.

        Args:
            key (str): Redis key.

        Returns:
            any: Deserialized value, or None if key doesn't exist.
        """
        value = self.client.get(key)
        return json.loads(value) if value else None

    def delete(self, key):
        """
        Delete a key from Redis.

        Args:
            key (str): Redis key.

        Returns:
            bool: True if key was deleted, False otherwise.
        """
        return self.client.delete(key) > 0
