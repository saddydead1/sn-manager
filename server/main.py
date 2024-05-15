from socket import *

serv_addr = 'localhost'
port = 7072
count_listens = 2


def main():

    server = socket(
        AF_INET, SOCK_STREAM
    )
    server.bind(
        (serv_addr, port)
    )
    server.listen(count_listens)

    print('SONOMA MANAGER STARTED')

    try:
        user, addr = server.accept()

        print(f'CONNECTED: {user}, {addr}')

    except Exception as e:
        print(f'ERROR: {e}')


if __name__ == "__main__":
    main()