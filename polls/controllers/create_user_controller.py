from polls.models.user import User
from polls.repository.user_repository import UserRepository


class CreateUserController:

    def __init__(self, owner_dto) -> None:
        self._owner_dto = owner_dto

    def create(self):
        user = User(
            first_name=self._owner_dto.first_name,
            last_name=self._owner_dto.last_name,
            username=self._owner_dto.username,
        )
        UserRepository().add(user)
        return user
