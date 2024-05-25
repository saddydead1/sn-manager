import requests
from user import User
import login_screen

addr = "127.0.0.1"
port = 7072


def login(user: User) -> bool:
    r = requests.get(f"http://{addr}:{str(port)}/log_in?user={user.username}&password={user.password}")

    if r.ok:
        login_screen.log_in = True
        print(login_screen.log_in)
        return True
    else:
        return False
