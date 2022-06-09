from polls.controllers import CreateQuestionController
from polls.repository.question_repository import QuestionRepository


def test_get_all_question(repository_transaction):
    CreateQuestionController(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    
    CreateQuestionController(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()

    assert len(QuestionRepository().get_all()) == 2


def test_when_there_are_no_questions():
    questions = QuestionRepository().get_all()

    assert len(questions) == 0