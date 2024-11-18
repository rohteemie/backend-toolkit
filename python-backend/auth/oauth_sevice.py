import requests
from .errors import AuthError

class OAuthService:
    """OAuth integration for third-party authentication."""

    def __init__(self, provider_config):
        """
        Initialize with provider configuration.

        Args:
            provider_config (dict): Config for OAuth provider (e.g., Google).
        """
        self.client_id = provider_config.get("client_id")
        self.client_secret = provider_config.get("client_secret")
        self.token_url = provider_config.get("token_url")
        self.user_info_url = provider_config.get("user_info_url")
        if not all([self.client_id, self.client_secret, self.token_url, self.user_info_url]):
            raise AuthError("Invalid OAuth provider configuration")

    def exchange_code_for_token(self, code, redirect_uri):
        """
        Exchange authorization code for access token.

        Args:
            code (str): Authorization code.
            redirect_uri (str): Redirect URI registered with the provider.

        Returns:
            dict: Token response.
        """
        try:
            response = requests.post(
                self.token_url,
                data={
                    "code": code,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "redirect_uri": redirect_uri,
                    "grant_type": "authorization_code",
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise AuthError(f"Failed to exchange code for token: {e}")

    def get_user_info(self, access_token):
        """
        Retrieve user information using the access token.

        Args:
            access_token (str): OAuth access token.

        Returns:
            dict: User information.
        """
        try:
            response = requests.get(
                self.user_info_url,
                headers={"Authorization": f"Bearer {access_token}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise AuthError(f"Failed to retrieve user info: {e}")
