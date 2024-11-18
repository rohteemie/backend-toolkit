from auth.oauth_service import OAuthService

oauth_service = OAuthService(google_config)

# Step 1: Exchange authorization code for access token
code = "received_authorization_code"
redirect_uri = "http://localhost/callback"
token_response = oauth_service.exchange_code_for_token(code, redirect_uri)
print("Token Response:", token_response)

# Step 2: Fetch user information
access_token = token_response["access_token"]
user_info = oauth_service.get_user_info(access_token)
print("User Info:", user_info)
