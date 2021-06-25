from user import User
from flask import Flask, request
from user_repository import UserRepository

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def addUser():
    return UserRepository().create(User(request.get_json().get('id'),request.get_json().get('name')))

@app.route('/',methods=['GET'])
def getUserById():
    return UserRepository().find(int(request.args.get('id')))