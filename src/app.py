from flask_lambda import FlaskLambda
from users.domain.user_exception import UserException
from users.infrastructure.api.exception_handler import handle_exception
from users.infrastructure.api.users_blueprint import create_users_blueprint
from config import configure_inject
from flask_cors import CORS

app = FlaskLambda(__name__)
CORS(app)
configure_inject(app)

app.register_error_handler(UserException,handle_exception)

app.register_blueprint(create_users_blueprint(), url_prefix='/users')

    