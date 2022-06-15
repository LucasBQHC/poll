class UserRepository:

    _users = []

    def add(self, user):
        self._users.append(user)
