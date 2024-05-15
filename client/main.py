from socket import *

addr = 'localhost'
port = 7072


def main():
    client = socket(
        AF_INET, SOCK_STREAM
    )

    client.connect((addr, port))


if __name__ == '__main__':
    main()

