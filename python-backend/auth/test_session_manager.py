import uuid
from datetime import datetime, timedelta

class SessionManager:
    """Manages user sessions."""

    def __init__(self, expiry_minutes=60):
        self.sessions = {}  # Replace with a persistent store like Redis if needed
        self.expiry_minutes = expiry_minutes

    def create_session(self, user_id):
        """
        Create a new session for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: Session details, including session ID and expiry.
        """
        session_id = str(uuid.uuid4())
        expiry_time = datetime.utcnow() + timedelta(minutes=self.expiry_minutes)
        self.sessions[session_id] = {"user_id": user_id, "expires_at": expiry_time}
        return {"session_id": session_id, "expires_at": expiry_time}

    def get_session(self, session_id):
        """
        Retrieve a session by its ID.

        Args:
            session_id (str): The session ID.

        Returns:
            dict: The session data if valid, or None if expired or not found.
        """
        session = self.sessions.get(session_id)
        if session and session["expires_at"] > datetime.utcnow():
            return session
        # Clean up expired session
        self.sessions.pop(session_id, None)
        return None

    def delete_session(self, session_id):
        """
        Delete a session.

        Args:
            session_id (str): The session ID.

        Returns:
            bool: True if session was deleted, False otherwise.
        """
        return self.sessions.pop(session_id, None) is not None
