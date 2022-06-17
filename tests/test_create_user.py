from polls.controllers import CreateUserController


def test_create_user(owner_dto):
    user = CreateUserController(
        owner_dto=owner_dto
    ).create()
    assert user.get_first_name() == 'Homero'
    assert user.get_last_name() == 'Simpson'
    assert user.get_username() == 'mr_x'
