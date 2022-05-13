from polls.controllers import create_question_controller
from polls.models.poll import Poll
from polls.repository import PollRepository


def create_poll_controller(poll_title, question_title, choices):
    poll = Poll(title=poll_title)
    question = create_question_controller(
        title=question_title,
        choices=choices
    )
    poll.add_question(question=question)
    repository = PollRepository()
    repository.add(poll)
    return poll