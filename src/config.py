from flask import Flask
import inject
from users.domain.user_database import UserDatabase
from users.infrastructure.database.user_dynamodb import UserDynamoDB

def configure_inject(app: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(UserDatabase, UserDynamoDB())

    inject.configure(config)