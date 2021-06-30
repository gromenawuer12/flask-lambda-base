from ...domain.user_database import UserDatabase

class UserInMemory(UserDatabase):
    def __init__(self):
        self.database = {0:{"nickname":"John","role":"admin"},1:{"nickname":"Pepito","role":"user"}}

    def create(self, user):
        self.database[list(self.database.keys())[-1]+1] = {"nickname":user.nickname,"role":user.role}
        return "Added"

    def find(self, id):
        return self.database.get(id)