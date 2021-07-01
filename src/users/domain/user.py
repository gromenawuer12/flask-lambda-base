from .user_error import UserError
import re

class User:
    def __init__(self, params):
        self.nickname = params.nickname
        self.role = params.role

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        if re.search(r"\W",nickname):
            raise UserError('User can only contain ')
        self.__nickname = nickname
            