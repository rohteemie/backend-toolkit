class AuthError(Exception):
    """Custom exception for authentication errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"AuthError: {self.message}"
