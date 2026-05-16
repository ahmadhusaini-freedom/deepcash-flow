import os

class Settings:
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
    YOUTUBE_REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN", "")
    YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID", "")
    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET", "")
    GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "")
    IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN", "")
    IG_USER_ID = os.getenv("IG_USER_ID", "")
    FALLBACK_TOPICS = [
        "Cara menghasilkan uang dari internet",
        "Investasi saham untuk pemula",
        "Tips menabung agar cepat kaya",
    ]