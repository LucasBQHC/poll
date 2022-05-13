from polls.db import poll_list
from polls.controllers import create_question_controller


def test_create_question():
    question = create_question_controller(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
            'choice four'
        ]
    )
    assert question.get_title() == 'Some question'
    assert question._choices[0]._text == 'choice one'
    assert question._choices[0]._votes == 0
    assert question._choices[1]._text == 'choice two'
    assert question._choices[1]._votes == 0
    assert question._choices[2]._text == 'choice three'
    assert question._choices[2]._votes == 0
    assert question._choices[3]._text == 'choice four'
    assert question._choices[3]._votes == 0

    poll_list.clear()