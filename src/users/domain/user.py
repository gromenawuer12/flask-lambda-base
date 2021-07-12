from .user_role import UserRole
from werkzeug.security import generate_password_hash
import sys

class User(UserRole):
    def __init__(self, params):
        super(User,self).__init__(params)
        self.password = params['password']
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = generate_password_hash(password,method='sha256')
            