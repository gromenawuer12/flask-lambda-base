import inject
from flask import Blueprint, Response, request, jsonify
from ...application.add_user import AddUser
from ...application.get_user import GetUser
from ...domain.user import User

@inject.autoparams()
def create_users_blueprint(get_user: GetUser, add_user: AddUser) -> Blueprint:
    users_blueprint = Blueprint('users', __name__)

    @users_blueprint.route('/',methods=['GET'])
    def get() -> Response:
        user = get_user.execute(int(request.args.get('id')))
        return jsonify(user)

    @users_blueprint.route('/add',methods=['POST'])
    def post() -> Response:
        return add_user.execute(User(request.get_json().get('id'),request.get_json().get('name')))


    return users_blueprint