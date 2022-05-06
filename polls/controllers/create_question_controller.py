from db import poll_list
from polls.models.question import Question


def create_question_controller(
            title,
            choice_one,
            choice_two,
            choice_three,
            choice_four):
    question = Question(
        title=title
        )
    question.add_choice(
        choice_one=choice_one,
        choice_two=choice_two,
        choice_three=choice_three,
        choice_four=choice_four
    )
    poll_list.append(question)
    return question
