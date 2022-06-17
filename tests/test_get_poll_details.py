from polls.controllers import CreateQuestionController
from polls.controllers import CreateUserController
from polls.controllers import GetPollDetailsController
from polls.repository import PollRepository
from polls.models.poll import Poll


def test_get_poll(poll_repository_transaction):
    owner = CreateUserController(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x'
    ).create()
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    question = CreateQuestionController(
        title='Question title',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    poll.add_question(question=question)
    PollRepository().add(poll=poll)
    poll_details = GetPollDetailsController().get_by_id(id=poll.get_id())

    assert poll_details.get_title() == poll.get_title()
    assert poll_details.get_owner() == poll.get_owner()
    assert poll_details.get_publication_date() is None
    assert poll_details.get_state() == poll.get_state()
    assert poll_details.get_questions() == poll.get_questions()
    assert poll_details.get_questions()[0].get_choices() == poll.get_questions()[0].get_choices()


def test_get_all_polls(poll_repository_transaction):
    owner = CreateUserController(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x'
    ).create()
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    question = CreateQuestionController(
        title='Question title',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    poll.add_question(question=question)
    PollRepository().add(poll=poll)

    owner = CreateUserController(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x'
    ).create()
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    poll = Poll(
        title='Poll title',
        owner=owner
    )
    question = CreateQuestionController(
        title='Question title',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    poll.add_question(question=question)
    PollRepository().add(poll=poll)

    assert len(PollRepository().get_all()) == 2
