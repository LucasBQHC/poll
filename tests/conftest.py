from pytest import fixture
from polls.controllers.create_user_controller import CreateUserController
from polls.controllers.owner_dto import OwnerDTO
from polls.repository.poll_repository import PollRepository

from polls.repository.question_repository import QuestionRepository


@fixture
def question_repository_transaction():
    yield
    QuestionRepository().clear_all()


@fixture
def poll_repository_transaction():
    yield
    PollRepository().clear_all()


@fixture
def owner_dto():
    return OwnerDTO(
        first_name='Homero',
        last_name='Simpson',
        username='mr_x',
    )


@fixture
def owner_fixture(owner_dto):
    return CreateUserController(owner_dto=owner_dto)
