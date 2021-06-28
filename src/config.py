from flask import Flask
import inject
from .users.domain.user_database import UserDatabase
from .users.infrastructure.database.user_in_memory import UserInMemory

def configure_inject(app: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(UserDatabase, UserInMemory())

    inject.configure(config)