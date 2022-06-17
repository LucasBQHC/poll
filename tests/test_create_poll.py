from constants import PollStatus
from polls.controllers import CreatePollController


def test_create_poll(question_repository_transaction, owner_dto):
    poll = CreatePollController(
        poll_title='Poll title',
        owner_dto=owner_dto,
        question_title='Question title',
        choices=[
            'Choice one',
            'Choice two',
            'Choice three',
        ]
    ).create()

    assert poll.get_title() == 'Poll title'
    assert poll.get_owner().get_first_name() == 'Homero'
    assert poll.get_owner().get_last_name() == 'Simpson'
    assert poll.get_owner().get_username() == 'mr_x'
    assert poll.get_state() == PollStatus.DRAFT
    assert poll.get_questions()[0].get_title() == 'Question title'
    assert poll.get_questions()[0].get_choices()[0].get_text() == 'Choice one'
    assert poll.get_questions()[0].get_choices()[1].get_text() == 'Choice two'
    assert poll.get_questions()[0].get_choices()[2].get_text() == 'Choice three'
