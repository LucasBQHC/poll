import uuid

from polls.controllers import get_question_controller


def get_question_command():
    id = uuid.UUID(input('Question id: '))
    question = get_question_controller(id)
    if question:
        print(
            f"""
            Title: {question.title}.
            Pub. date: {question.publication_date}.

            Choices & votes:

                Choice: {question.choices['choice_one']['choice_text']}.
                    - Total votes: {question.choices['choice_one']['vote']}.

                Choice: {question.choices['choice_two']['choice_text']}.
                    - Total votes: {question.choices['choice_two']['vote']}.

                Choice: {question.choices['choice_three']['choice_text']}.
                    - Total votes: {question.choices['choice_three']['vote']}.

                Choice: {question.choices['choice_four']['choice_text']}.
                    - Total votes: {question.choices['choice_four']['vote']}.
            """)
    else:
        print('Question does not exist')
