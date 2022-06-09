from polls.controllers import GetQuestionController
from polls.controllers import CreateQuestionController
from polls.repository.question_repository import QuestionRepository


def test_get_question(repository_transaction):
    question = CreateQuestionController(
        title='Some title',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    q = GetQuestionController().get_by_id(question.get_id())

    assert q.get_id() == question.get_id()
    assert q.get_title() == 'Some title'
    assert q.get_choices()[0].get_text() == 'choice one'
    assert q.get_choices()[0].get_votes() == 0
    assert q.get_choices()[1].get_text() == 'choice two'
    assert q.get_choices()[1].get_votes() == 0
    assert q.get_choices()[2].get_text() == 'choice three'
    assert q.get_choices()[2].get_votes() == 0


def test_when_id_does_not_exists():
    question = GetQuestionController().get_by_id(
        '3a6384fc-2b57-461f-814f-7542b2953c5f'
    )

    assert question == None