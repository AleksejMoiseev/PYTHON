import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 8888))
    sock.listen(4)
    client, addres = sock.accept()
    result = b''
    chunk = b'1'
    while chunk != b'':
        chunk = client.recv(1024)
        result += chunk

    print(result.decode("utf-8"))
    client.close()