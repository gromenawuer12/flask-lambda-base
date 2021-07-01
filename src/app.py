from flask_lambda import FlaskLambda
from users.domain.user_error import UserError
from users.infrastructure.api.exception_handler import handle_exception
from users.infrastructure.api.users_blueprint import create_users_blueprint
from config import configure_inject

app = FlaskLambda(__name__)
configure_inject(app)

app.register_error_handler(UserError,handle_exception)

app.register_blueprint(create_users_blueprint(), url_prefix='/users')

    