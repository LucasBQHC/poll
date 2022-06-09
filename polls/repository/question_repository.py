

class QuestionRepository:

    _questions = []

    def add(self, question):
        self._questions.append(question)
    
    def get_all(self):
        return tuple(self._questions)

    def get_by_id(self, id):
        for question in self._questions:
            if question.get_id() == id:
                return question

    def clear_all(self):
        self._questions.clear()