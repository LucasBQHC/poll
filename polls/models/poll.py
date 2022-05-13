from .question import Question


class Poll:

    def __init__(self, title):
        self._title = title
        self._publication_date = None
        self._state = 'draft'
        self._questions = []

    def get_title(self):
        return self._title

    def get_publication_date(self):
        return self._publication_date

    def get_state(self):
        return self._state

    def get_questions(self):
        return tuple(self._questions)
    
    def add_question(self, question):
        assert isinstance(question, Question)
        self._questions.append(question)
