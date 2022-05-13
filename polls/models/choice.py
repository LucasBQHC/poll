

class Choice:

    def __init__(self, text: str):
        self._text = text
        self._votes = 0

    def get_text(self):
        return self._text

    def get_votes(self):
        return self._votes
