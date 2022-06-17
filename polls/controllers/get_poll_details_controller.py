from polls.repository import PollRepository


class GetPollController:

    def get_by_id(self, id):
        return PollRepository().get_by_id(id=id)

    def get_all(self):
        return PollRepository().get_all()
