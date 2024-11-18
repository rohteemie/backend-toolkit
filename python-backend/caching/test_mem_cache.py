from cache.memory_cache import MemoryCache

cache = MemoryCache()
cache.set("session_1", {"user_id": 123}, ttl=3600)
session = cache.get("session_1")
print(session)  # Output: {"user_id": 123}
