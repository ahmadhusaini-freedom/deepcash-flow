class TrendFinder:
    def __init__(self, settings):
        self.settings = settings

    def get_trending_topics(self, count=3):
        return self.settings.FALLBACK_TOPICS[:count]