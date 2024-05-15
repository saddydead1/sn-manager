from socket import *

serv_addr = 'localhost'
port = 7072
count_listens = 2


class Server:
    def __init__(self, ip, port, listens):
        self.server = socket(
            AF_INET, SOCK_STREAM
        )
        self.server.bind((ip, port))
        self.server.listen(listens)

    def start_server(self):
        while True:
            user, addr = self.server.accept()
            print(f'connected: {user}, {addr}')
            user.send('connected'.encode('utf-8'))


def main():
    Server(serv_addr, port, count_listens).start_server()


if __name__ == "__main__":
    main()
