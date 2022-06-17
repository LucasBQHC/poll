from polls.controllers import CreateQuestionController, CreateUserController, GetPollController
from polls.controllers.owner_dto import OwnerDTO
from polls.repository import PollRepository
from polls.models.poll import Poll


def test_get_poll(poll_repository_transaction):
    owner_dto = OwnerDTO(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x',
    )
    owner = CreateUserController(
        owner_dto=owner_dto
    ).create()
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
    poll_details = GetPollController().get_by_id(id=poll.get_id())

    assert poll_details.get_title() == poll.get_title()
    assert poll_details.get_owner() == poll.get_owner()
    assert poll_details.get_publication_date() is None
    assert poll_details.get_state() == poll.get_state()
    assert poll_details.get_questions() == poll.get_questions()
    assert poll_details.get_questions()[0].get_choices() == poll.get_questions()[0].get_choices()


def test_get_all_polls(poll_repository_transaction, owner_fixture):
    poll = Poll(
        title='Poll title',
        owner=owner_fixture
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

    owner_dto = OwnerDTO(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x',
    )
    owner = CreateUserController(
        owner_dto=owner_dto
    ).create()
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
