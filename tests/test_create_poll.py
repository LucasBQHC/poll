from constants import PollStatus
from polls.controllers import CreatePollController
from polls.repository.question_repository import QuestionRepository


def test_create_poll(repository_transaction):
    poll = CreatePollController(
        poll_title='Poll title',
        question_title='Question title',
        choices=[
            'Choice one',
            'Choice two',
            'Choice three',
        ]
    ).create()

    assert poll.get_title() == 'Poll title'
    assert poll.get_state() == PollStatus.DRAFT
    assert poll.get_questions()[0].get_title() == 'Question title'
    assert poll.get_questions()[0].get_choices()[0].get_text() == 'Choice one'
    assert poll.get_questions()[0].get_choices()[1].get_text() == 'Choice two'
    assert poll.get_questions()[0].get_choices()[2].get_text() == 'Choice three'