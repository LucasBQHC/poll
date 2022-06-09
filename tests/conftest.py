from pytest import fixture

from polls.repository.question_repository import QuestionRepository


@fixture
def repository_transaction():
    yield 
    QuestionRepository().clear_all()