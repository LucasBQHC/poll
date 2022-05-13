from polls.controllers import create_poll_controller


def create_poll_command():
    poll_title = input('Poll title: ')
    question_title = input('Question title: ')
    choice_one = input('Choice one: ')
    choice_two = input('Choice two: ')
    choice_three = input('Choice three: ')
    choice_four = input('Choice four: ')
    
    create_poll_controller(
        poll_title,
        question_title,
        choices=[
            choice_one,
            choice_two,
            choice_three,
            choice_four
        ]
    )