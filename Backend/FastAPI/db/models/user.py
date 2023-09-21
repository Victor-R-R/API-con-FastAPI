"""### User model ###"""

from pydantic import BaseModel


class User(BaseModel):
    """ Este módulo contiene una función que crea un usuario."""

    def __init__(self, name, username, email):
        super().__init__()
        self.name = name
        self.username = username
        self.email = email
