from polls.controllers import CreatePollController


def create_poll_command():
    poll_title = input('Poll title: ')
    question_title = input('Question title: ')
    choice_one = input('Choice one: ')
    choice_two = input('Choice two: ')
    choice_three = input('Choice three: ')
    
    CreatePollController(
        poll_title,
        question_title,
        choices=[
            choice_one,
            choice_two,
            choice_three,
        ]
    ).create()