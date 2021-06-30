import inject, json
from mapper.object_mapper import ObjectMapper
from types import SimpleNamespace
from flask import Blueprint, Response, request, jsonify
from ...application.add_user import AddUser
from ...application.get_user import GetUser
from ...domain.user import User

@inject.autoparams()
def create_users_blueprint(get_user: GetUser, add_user: AddUser) -> Blueprint:
    users_blueprint = Blueprint('users', __name__)

    @users_blueprint.route('/<id>',methods=['GET'])
    def get(id) -> Response:
        return jsonify(get_user.execute(int(id)))

    @users_blueprint.route('/',methods=['POST'])
    def post() -> Response:
        userSimple =  json.loads(json.dumps(request.get_json()),object_hook=lambda d: SimpleNamespace(**d))
        mapper = ObjectMapper()
        mapper.create_map(SimpleNamespace, User)
        user = mapper.map(userSimple, User)
        return add_user.execute(user)


    return users_blueprint