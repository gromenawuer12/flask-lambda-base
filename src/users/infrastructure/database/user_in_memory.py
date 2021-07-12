from ...domain.user_database import UserDatabase
import sys

class UserInMemory(UserDatabase):
    def __init__(self):
        self.database = {"John":{"username":"John","role":"admin","password":"nlkhyt"},
        "Pepito":{"username":"Pepito","role":"user","password":"kajdfsg"},
        "test":{"username":"test","password":"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08","role":"test"}}

    def create(self, user):
        self.database[user.username] = {"username":user.username,"password":user.password,"role":user.role}
        return "Added"

    def find(self, username):
        return self.database.get(username)
    
    def delete(self, username):
        del(username)
        return "Deleted"