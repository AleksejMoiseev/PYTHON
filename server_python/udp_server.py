import socket

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port.bind(('127.0.0.1', 8888))
result = port.recv(1024)
print("Message: ", result.decode(encoding='utf-8'))
port.close()
