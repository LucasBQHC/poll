

class PollRepository:

    _polls = []

    def add(self, poll):
        self._polls.append(poll)