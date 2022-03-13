import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socks:
    socks.bind(("127.0.0.1", 8888))

    while True:
        result = socks.recv(1024)
        print(result)