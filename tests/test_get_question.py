from polls.db import poll_list
from polls.controllers import get_question_controller
from polls.controllers.create_question_controller import create_question_controller


def test_get_question():
    question = create_question_controller(
        title='Some title',
        choices=[
            'choice one',
            'choice two',
            'choice three',
            'choice four'
        ]
    )
    q = get_question_controller(question._id)

    poll_list.clear()

    assert q._id == question._id
    assert q._title == 'Some title'
    assert q._choices[0]._text == 'choice one'
    assert q._choices[0]._votes == 0
    assert q._choices[1]._text == 'choice two'
    assert q._choices[1]._votes == 0
    assert q._choices[2]._text == 'choice three'
    assert q._choices[2]._votes == 0
    assert q._choices[3]._text == 'choice four'
    assert q._choices[3]._votes == 0


def test_when_id_does_not_exists():
    question = get_question_controller('3a6384fc-2b57-461f-814f-7542b2953c5f')

    assert question == None