import requests
from user import User
import login_screen

addr = "127.0.0.1"
port = 7072


def is_login(user: User) -> bool:
    r = requests.get(f"http://{addr}:{str(port)}/log_in?user={user.username}&password={user.password}")

    if r.ok:
        return True
    else:
        return False
