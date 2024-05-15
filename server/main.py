import eventlet
import socketio

addr = 'localhost'
port = 7072


class Server:
    def __init__(self):
        self.sio = socketio.Server()
        self.app = socketio.WSGIApp(self.sio, static_files={
            '/': {'content_type': 'text/html', 'filename': 'index.html'}
        })

    def start_server(self):
        eventlet.wsgi.server(eventlet.listen((addr, port)), self.app)


if __name__ == '__main__':
    Server().start_server()
