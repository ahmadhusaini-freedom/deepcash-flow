import anthropic

class ScriptWriter:
    def __init__(self, settings):
        self.client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)

    def generate_script(self, topic):
        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": f"Buat konten singkat tentang: {topic}"}]
        )
        return message.content[0].text