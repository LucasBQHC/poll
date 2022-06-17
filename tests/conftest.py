from pytest import fixture
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
