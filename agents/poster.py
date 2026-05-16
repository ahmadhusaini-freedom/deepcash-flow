class ContentPoster:
    def __init__(self, settings):
        self.settings = settings

    def post_all(self, item):
        return {
            "youtube": {"success": True, "message": "Skipped (no video)"},
            "instagram": {"success": True, "message": "Skipped (no token)"},
        }