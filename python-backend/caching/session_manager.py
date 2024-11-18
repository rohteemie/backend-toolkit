from cache.redis_cache import RedisCache
from uuid import uuid4

class SessionManager:
    """Manages user sessions using Redis as the backend."""
    def __init__(self):
        self.cache = RedisCache()

    def create_session(self, user_id):
        """Create a new session for a user."""
        session_id = str(uuid4())  # Generate a unique session ID
        self.cache.set(session_id, user_id, ttl=3600)  # Session valid for 1 hour
        return session_id

    def get_user(self, session_id):
        """Retrieve the user ID associated with a session ID."""
        user_id = self.cache.get(session_id)
        if user_id:
            return user_id.decode()  # Decode byte response
        return None

    def delete_session(self, session_id):
        """Delete a session."""
        self.cache.delete(session_id)

    def clear_sessions(self):
        """Clear all sessions."""
        self.cache.clear()
