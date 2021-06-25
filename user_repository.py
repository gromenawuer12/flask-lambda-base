class UserRepository:
    def __init__(self):
        self.database = {0:"John",1:"Pepito"}

    def create(self, user):
        self.database[user.id]=user.name
        return "Added"

    def find(self, id):
        return self.database.get(id)