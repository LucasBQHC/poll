from polls.controllers import CreateQuestionController
from polls.controllers.create_user_controller import CreateUserController
from polls.models.poll import Poll
from polls.repository import PollRepository


class CreatePollController:

    def __init__(self, poll_title, owner_first_name, owner_last_name, owner_username, question_title, choices) -> None:
        self._poll_title = poll_title
        self._owner_first_name = owner_first_name
        self._owner_last_name = owner_last_name
        self._owner_username = owner_username
        self._question_title = question_title
        self._choices = choices

    def create(self):
        owner = CreateUserController(
            first_name=self._owner_first_name,
            last_name=self._owner_last_name,
            username=self._owner_username
        ).create()
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
