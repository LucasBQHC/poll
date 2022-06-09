from polls.controllers import CreateQuestionController


def create_question_command():
    title = input('Title: ')
    choice_one = input('Choice one: ')
    choice_two = input('Choice two: ')
    choice_three = input('Choice three: ')

    CreateQuestionController(
        title,
        choices=[
            choice_one,
            choice_two,
            choice_three,
        ]
    ).create()
