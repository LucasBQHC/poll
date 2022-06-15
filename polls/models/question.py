import uuid

from .choice import Choice


class Question:

    def __init__(self, title: str) -> None:
        self._id = str(uuid.uuid4())
        self._title = title
        self._choices = []

    def add_choice(self, choice):
        assert isinstance(choice, Choice)
        self._choices.append(choice)

    def get_title(self):
        return self._title

    def get_id(self):
        return self._id

    def get_choices(self):
        return tuple(self._choices)
