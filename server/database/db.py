import sqlite3

from server.user import User

con = sqlite3.connect('database/users.db', check_same_thread=False)
cur = con.cursor()


def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL, password TEXT NOT NULL)")


def create_user(user: User):
    print(user.username, user.password)
    cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (user.username, user.password))
    con.commit()


def log_in(user: User) -> bool:
    cur.execute('SELECT password FROM users WHERE username=?', (user.username, ))
    password = cur.fetchone()
    if password[0] == user.password:
        return True
    else:
        return False
