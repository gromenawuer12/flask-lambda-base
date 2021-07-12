import inject
from ..domain.user import User
from ..domain.user_role import UserRole
from ..domain.user_name import UserName
from ..domain.user_database import UserDatabase

class GetUser:
    @inject.autoparams()
    def __init__(self, database: UserDatabase):
        self.__database = database

    def execute(self, username, auth_username):
        user = self.__database.find(username)
        if auth_username is None:
            return UserName(user)
        if username!=auth_username:
            return UserRole(user) 
        return User(user)