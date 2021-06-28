from flask import Flask
from .users.infrastructure.api.users_blueprint import create_users_blueprint
from .config import configure_inject

def create_app() -> Flask:
    app = Flask(__name__)
    configure_inject(app)

    app.register_blueprint(create_users_blueprint(), url_prefix='/api')

    return app