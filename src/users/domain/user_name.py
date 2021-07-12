from .user_exception import UserException
import re, sys

class UserName():
    def __init__(self, params):
        self.username = params['username']
       
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if re.search(r"\W",username):
            raise UserException('Username can only contain alphanumeric values and low slashes')
        self._username = username
        