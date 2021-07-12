from werkzeug.security import check_password_hash, generate_password_hash
import inject, json, jwt, datetime, os, sys
from types import SimpleNamespace
from flask import Blueprint, Response, request
from users.application.login_user import LoginUser
from .login_exception import LoginException
from ...application.add_user import AddUser
from ...application.get_user import GetUser
from ...application.delete_user import DeleteUser
from ...domain.user import User
from .token_optional_decorator import token_optional
from .token_required_decorator import token_required


@inject.autoparams()
def create_users_blueprint(get_user: GetUser, add_user: AddUser,login_user: LoginUser, delete_user: DeleteUser) -> Blueprint:
    users_blueprint = Blueprint('users', __name__)

    @users_blueprint.route('/<username>',methods=['GET'])
    @token_optional
    def get(auth_username,username) -> Response:
        return get_user.execute(username, auth_username).__dict__

    @users_blueprint.route('/',methods=['POST'])
    def post() -> Response:
        return add_user.execute(User(json.loads(json.dumps(request.get_json()),object_hook=lambda d: SimpleNamespace(**d).__dict__)))

    @users_blueprint.route('/login',methods=['POST'])
    def login() -> Response:
        auth = request.authorization
        if auth is None:
            raise LoginException("Invalid login")
        user = login_user.execute(auth.get('username'))
        if user is None or not check_password_hash(user['password'],auth.password):
            raise LoginException("Invalid username or password")
        return jwt.encode({'username': user['username'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30),}, os.getenv('SECRET_KEY'),algorithm="HS256")

    @users_blueprint.route('/<username>',methods=['PUT'])
    @token_required
    def modify(auth_username, username) -> Response:    
        if auth_username!=username:
            raise Exception
        user = get_user.execute(auth_username,username).__dict__
        new_username = request.get_json().get("new_username") if request.get_json().get("new_username") else user['_username']
        new_password = request.get_json().get("new_password") if request.get_json().get("new_password") else user['_password']
        new_role = request.get_json().get("new_role") if request.get_json().get("new_role") else user['role']

        delete_user.execute(user['username'])
        add_user.execute(User({"username":new_username,"role":new_role,"password":new_password}))
        return "Updated"

    return users_blueprint