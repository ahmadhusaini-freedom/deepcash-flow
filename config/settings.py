import os

class Settings:
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "")
    YOUTUBE_REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN", "")
    YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID", "")
    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET", "")
    GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "")
    IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN", "")
    IG_USER_ID = os.getenv("IG_USER_ID", "")

    # Niche konten sesuai brand @abuya_zaky
    FALLBACK_TOPICS = [
        "Tips membangun personal branding yang kuat",
        "Cara menghasilkan uang dari media sosial",
        "Strategi investasi untuk pemula 2026",
        "Tips menabung dan mengelola keuangan",
        "Cara membangun bisnis online dari nol",
        "Tips sukses di Instagram dan TikTok",
        "Passive income untuk generasi muda",
        "Cara meningkatkan follower Instagram organik",
    ]

    # Affiliate links (isi setelah daftar)
    TOKOPEDIA_AFFILIATE = os.getenv("TOKOPEDIA_AFFILIATE", "")
    SHOPEE_AFFILIATE = os.getenv("SHOPEE_AFFILIATE", "")