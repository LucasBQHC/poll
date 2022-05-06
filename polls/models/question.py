import datetime
import uuid


class Question:
    def __init__(self, title: str,):
        self.id = uuid.uuid4()
        self.title = title
        self.publication_date = datetime.datetime.now()
        self.status = 'active'
        self.choices = []

    def add_choice(self, choice_one, choice_two, choice_three, choice_four):
        self.choices = {
            'choice_one': {
                'id': uuid.uuid4(),
                'choice_text': choice_one,
                'vote': 0,
            },
            'choice_two': {
                'id': uuid.uuid4(),
                'choice_text': choice_two,
                'vote': 0,
            },
            'choice_three': {
                'id': uuid.uuid4(),
                'choice_text': choice_three,
                'vote': 0,
            },
            'choice_four': {
                'id': uuid.uuid4(),
                'choice_text': choice_four,
                'vote': 0,
            },
        }
