from polls.controllers import GetQuestionController


def get_question_command():
    id = input('Question id: ')
    question = GetQuestionController().get_by_id(id)
    if question:
        print(
            f"""
            Title: {question.get_title()}.

            Choices & votes:

            {question.get_choices()}

            """)
    else:
        print('Question does not exist')