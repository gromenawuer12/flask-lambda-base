import inject,sys
from ..domain.user import User
from ..domain.nose_decorator import nose
from ..domain.user_database import UserDatabase
from ..domain.user_permissions import deleteAttrs

class GetUser:
    @inject.autoparams()
    def __init__(self, database: UserDatabase):
        self.__database = database
    @nose
    def execute(self, username, auth_username):
        user = self.__database.find(username)
        user = User(user)
        if auth_username is None:
            return deleteAttrs(user,["_password","role"])
        if username!=auth_username:
            return deleteAttrs(user,["_password"])
        return user