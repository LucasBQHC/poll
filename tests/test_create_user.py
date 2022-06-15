from polls.controllers import CreateUserController


def test_create_user():
    user = CreateUserController(
        first_name='first name',
        last_name='last name',
        username='username'
    ).create()
    assert user.get_first_name() == 'first name'
    assert user.get_last_name() == 'last name'
    assert user.get_username() == 'username'
