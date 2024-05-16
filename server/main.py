import uvicorn
from fastapi import FastAPI, Request, Body
from fastapi.responses import RedirectResponse, FileResponse

addr = '127.0.0.1'
port = 7072


class Server:
    def __init__(self):
        self.app = FastAPI()
        self.port = port
        self.addr = addr

    def start_server(self):
        uvicorn.run(self.app, port=self.port, proxy_headers=True)


if __name__ == '__main__':
    Server().start_server()