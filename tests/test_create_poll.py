from polls.controllers import create_poll_controller


def test_create_poll():
    poll = create_poll_controller(
        poll_title='Poll title',
        question_title='Question title',
        choices=[
            'Choice one',
            'Choice two',
            'Choice three',
            'Choice four',
        ]
    )

    assert poll.get_title() == 'Poll title'
    assert poll.get_state() == 'draft'
    assert poll._questions[0]._title == 'Question title'
    assert poll._questions[0]._choices[0]._text == 'Choice one'
    assert poll._questions[0]._choices[1]._text == 'Choice two'
    assert poll._questions[0]._choices[2]._text == 'Choice three'
    assert poll._questions[0]._choices[3]._text == 'Choice four'