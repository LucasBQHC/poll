from db import poll_list
from polls.controllers import create_question_controller


def test_create_question():
    question = create_question_controller(
        title='Some question',
        choice_one='choice one',
        choice_two='choice two',
        choice_three='choice three',
        choice_four='choice four',
    )
    assert question.title == 'Some question'
    assert question.status == 'active'
    assert question.choices['choice_one']['choice_text'] == 'choice one'
    assert question.choices['choice_one']['vote'] == 0
    assert question.choices['choice_two']['choice_text'] == 'choice two'
    assert question.choices['choice_two']['vote'] == 0
    assert question.choices['choice_three']['choice_text'] == 'choice three'
    assert question.choices['choice_three']['vote'] == 0
    assert question.choices['choice_four']['choice_text'] == 'choice four'
    assert question.choices['choice_four']['vote'] == 0
    poll_list.clear()
