from os import strerror
from .user_name import UserName
import sys

class UserRole(UserName):
    def __init__(self, params):
       super(UserRole,self).__init__(params)
       self.role = params['role']