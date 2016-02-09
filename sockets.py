import socket


def socketFunctions():
    # Returns host's name
    print socket.gethostname()

    # Returns ip address of host
    print socket.gethostbyname(socket.gethostname())


def main():
    socketFunctions()

if __name__ == '__main__':
    main()
