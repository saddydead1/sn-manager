import uvicorn
import containers
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from server.database import db
import security
from user import User

addr = '127.0.0.1'
port = 7072
app = FastAPI()


class Server:
    def __init__(self):
        self.port = port
        self.addr = addr

    @app.get("/")
    def doc(self: Request):
        return RedirectResponse(f'{self.url}docs')

    @app.get("/list_containers")
    def list_cont(self: Request, user: str, password: str):
        if security.log_in(User(user, password)):
            return str(containers.containers_list())
        else:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    @app.get("/log_in")
    def log_in(self: Request, user: str, password: str):
        if security.log_in(User(user, password)):
            raise HTTPException(status_code=200)
        else:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    def start_server(self):
        uvicorn.run(app, port=self.port, proxy_headers=True, host=self.addr)


if __name__ == '__main__':
    db.create_table()

    Server().start_server()
