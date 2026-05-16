class MediaFactory:
    def __init__(self, settings):
        self.settings = settings

    def create_thumbnail(self, topic, script):
        return f"thumbnail_{topic[:20]}.jpg"