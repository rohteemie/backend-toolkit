import bcrypt
import jwt
from datetime import datetime, timedelta
from os import getenv
from .errors import AuthError
from .utils import validate_email

class AuthService:
    """Authentication service with reusable components."""

    def __init__(self):
        """Initialize secret key and algorithm for JWT."""
        self.secret_key = getenv("JWT_SECRET", "default_secret")
        self.algorithm = getenv("JWT_ALGORITHM", "HS256")
        self.token_expiry_minutes = int(getenv("JWT_EXPIRY_MINUTES", 60))

    def hash_password(self, plain_password):
        """Hash a password using bcrypt."""
        if not plain_password:
            raise AuthError("Password cannot be empty")
        return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify_password(self, plain_password, hashed_password):
        """Verify a password against a hashed value."""
        if not plain_password or not hashed_password:
            raise AuthError("Invalid password provided")
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    def create_token(self, user_id, additional_payload=None):
        """
        Create a JWT for a given user ID.

        Args:
            user_id (str): The user ID.
            additional_payload (dict): Optional additional claims.

        Returns:
            str: Encoded JWT token.
        """
        if not user_id:
            raise AuthError("User ID is required for token creation")

        payload = {
            "sub": user_id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=self.token_expiry_minutes)
        }

        if additional_payload:
            payload.update(additional_payload)

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token):
        """
        Decode and validate a JWT.

        Args:
            token (str): The JWT.

        Returns:
            dict: Decoded payload.
        """
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            raise AuthError("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthError("Invalid token")

    def authenticate_user(self, email, password, user_repository):
        """
        Authenticate a user by email and password.

        Args:
            email (str): User's email.
            password (str): User's password.
            user_repository (callable): A function to fetch user details by email.

        Returns:
            dict: Authenticated user details and token.
        """
        if not validate_email(email):
            raise AuthError("Invalid email format")

        user = user_repository(email)
        if not user or not self.verify_password(password, user.get("password")):
            raise AuthError("Invalid email or password")

        token = self.create_token(user["id"])
        return {"user": user, "token": token}
