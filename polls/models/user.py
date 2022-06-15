class User:

    def __init__(self, first_name: str, last_name: str, username: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._username = username

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_username(self):
        return self._username
