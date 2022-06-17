from polls.controllers import CreateQuestionController
from polls.controllers.create_user_controller import CreateUserController
from polls.models.poll import Poll
from polls.repository import PollRepository


class CreatePollController:

    def __init__(self, poll_title, owner_dto, question_title, choices) -> None:
        self._poll_title = poll_title
        self._owner_dto = owner_dto
        self._question_title = question_title
        self._choices = choices

    def create(self):
        owner = CreateUserController(owner_dto=self._owner_dto).create()
        poll = Poll(
            title=self._poll_title,
            owner=owner
        )
        question = CreateQuestionController(
            title=self._question_title,
            choices=self._choices
        ).create()
        poll.add_question(question=question)
        PollRepository().add(poll)
        return poll
