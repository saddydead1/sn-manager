from database import db
from server.user import User


def create_user(username: str, password: str):
    user = User(username, password)
    db.create_user(user)


def log_in(user: User) -> bool:
    if db.log_in(user):
        return True
    else:
        return False

