import socket

port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port.connect(("127.0.0.1", 8080))
port.send(b'only latin characterddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
port.close()