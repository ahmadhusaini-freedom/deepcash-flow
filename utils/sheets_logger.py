class SheetsLogger:
    def __init__(self, settings):
        self.settings = settings

    def log(self, topic, result):
        print(f"  Log: {topic}")