from polls.controllers import create_question_controller


def create_question_command():
    title = input('Title: ')
    choice_one = input('Choice one: ')
    choice_two = input('Choice two: ')
    choice_three = input('Choice three: ')
    choice_four = input('Choice four: ')

    create_question_controller(
        title,
        choice_one,
        choice_two,
        choice_three,
        choice_four,
    )
