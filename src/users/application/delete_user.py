import inject
from ..domain.user_database import UserDatabase

class DeleteUser:
    @inject.autoparams()
    def __init__(self, database: UserDatabase):
        self.__database = database

    def execute(self, username) -> str:
        self.__database.delete(username)
        return "Deleted"