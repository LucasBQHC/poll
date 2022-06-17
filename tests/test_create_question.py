from polls.controllers import CreateQuestionController


def test_create_question(question_repository_transaction):
    question = CreateQuestionController(
        title='Some question',
        choices=[
            'choice one',
            'choice two',
            'choice three',
        ]
    ).create()
    assert question.get_title() == 'Some question'
    assert question.get_choices()[0].get_text() == 'choice one'
    assert question.get_choices()[0].get_votes() == 0
    assert question.get_choices()[1].get_text() == 'choice two'
    assert question.get_choices()[1].get_votes() == 0
    assert question.get_choices()[2].get_text() == 'choice three'
    assert question.get_choices()[2].get_votes() == 0
