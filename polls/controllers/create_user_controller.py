from polls.models.user import User
from polls.repository.user_repository import UserRepository


class CreateUserController:

    def __init__(self, first_name: str, last_name: str, username: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._username = username

    def create(self):
        user = User(
            first_name=self._first_name,
            last_name=self._last_name,
            username=self._username,
        )
        UserRepository().add(user)
        return user
