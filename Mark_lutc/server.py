import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)

client, addr = sock.accept()
result = client.recv(1024)
print(result)
client.close()
print( result.decode('utf-8'))
sock.close()