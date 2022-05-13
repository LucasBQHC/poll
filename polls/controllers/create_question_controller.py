from polls.db import poll_list
from polls.models.choice import Choice
from polls.models.question import Question


def create_question_controller(title, choices):
    question = Question(title=title)
    for choice in choices:
        question.add_choice(choice=Choice(text=choice))
    poll_list.append(question)
    return question
