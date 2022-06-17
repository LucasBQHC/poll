from polls import settings


class PollRepository:

    _polls = []

    def add(self, poll):
        self._polls.append(poll)

    def get_all(self):
        return tuple(self._polls)

    def get_by_id(self, id):
        for poll in self._polls:
            if poll.get_id() == id:
                return poll

    if settings.ENVIRONMENT == 'testing':
        def clear_all(self):
            self._polls.clear()
