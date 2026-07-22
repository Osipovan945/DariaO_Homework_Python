import os

# URL API
BASE_URL = "https://ru.yougile.com/api-v2"
AUTH_TOKEN = os.getenv(
    "YOUGILE_TOKEN",
    "your_token_here")

TEST_USER_ID = os.getenv("TEST_USER_ID", "your_user_id_here")
