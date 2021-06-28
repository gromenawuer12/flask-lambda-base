import inject
from ..domain.user import User
from ..domain.user_database import UserDatabase

class GetUser:
    @inject.autoparams()
    def __init__(self, database: UserDatabase):
        self.__database = database

    def execute(self, id) -> User:
        return self.__database.find(id)