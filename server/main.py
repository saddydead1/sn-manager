import uvicorn
from fastapi import FastAPI, Request, Body
from fastapi.responses import RedirectResponse, FileResponse

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

    def start_server(self):
        uvicorn.run(app, port=self.port, proxy_headers=True, host=self.addr)


if __name__ == '__main__':
    Server().start_server()
