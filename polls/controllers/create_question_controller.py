from polls.models.choice import Choice
from polls.models.question import Question
from polls.repository import QuestionRepository


class CreateQuestionController:

    def __init__(self, title: str, choices) -> None:
        self._title = title
        self._choices = choices

    def create(self):
        question = Question(title=self._title)
        for choice in self._choices:
            question.add_choice(choice=Choice(text=choice))
        QuestionRepository().add(question)
        return question
