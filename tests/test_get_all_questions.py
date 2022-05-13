from random import choices
from turtle import title
from polls.db import poll_list
from polls.controllers import create_question_controller, get_all_question_controller


def test_get_all_question():

    create_question_controller(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
            'choice four'
        ]
    )

    create_question_controller(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
            'choice four'
        ]
    )

    get_all_question_controller()

    assert len(poll_list) == 2

    poll_list.clear() 

def test_when_there_are_no_questions():
    questions =  get_all_question_controller()

    assert questions == []