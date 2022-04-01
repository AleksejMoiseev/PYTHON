import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('This is your IP address: ',ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name: ')


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())


# import gevent
# from gevent import socket
# urls = ['www.google.com', 'www.example.com', 'www.python.org']
# jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
# _ = gevent.joinall(jobs, timeout=2)
# [job.value for job in jo['74.125.79.106', '208.77.188.166', '82.94.164.162']
