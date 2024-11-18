from cache.memory_cache import MemoryCache

# Initialize the in-memory cache
cache = MemoryCache()

# Set a key-value pair with TTL of 5 seconds
cache.set("username", "john_doe", ttl=5)
print(cache.get("username"))  # Output: "john_doe"

# Wait for the key to expire
time.sleep(6)
print(cache.get("username"))  # Output: None

# Store multiple keys and check the count
cache.set("key1", "value1")
cache.set("key2", "value2", ttl=10)
print(cache.count())  # Output: 2

# Clear all entries
cache.clear()
print(cache.count())  # Output: 0
